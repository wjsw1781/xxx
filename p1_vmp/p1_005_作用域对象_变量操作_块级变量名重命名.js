/* eslint-disable no-case-declarations */

const fs = require("fs");

const parser = require("@babel/parser");
const traverse = require("@babel/traverse").default;
const generate = require("@babel/generator").default;

const INST = {};
{
  INST[(INST["ADD"] = 1)] = "ADD";

  INST[(INST["DEF"] = 50)] = "DEF";
  INST[(INST["STORE"] = 51)] = "STORE";
  INST[(INST["LAOD"] = 52)] = "LAOD";

  INST[(INST["PUSH"] = 101)] = "PUSH";

  INST[(INST["undefine"] = 151)] = "undefine";
}

// 编译器
class Complier {
  constructor(code) {
    this.ast = parser.parse(code);
    // 指令表
    this.instList = [];
    // 常量表
    this.poolList = [];
  }
  //重命名变量名---->作用域下的变量名 本身并没有重命名而是告诉栈(推入栈的时候用的是作用域名)
  toscopeName(id) {
    let { name, scope } = id;
    let s = scope;
    while (s) {
      let { bindings, uid } = s;
      if (bindings[name]) {
        return `zq${uid}_${name}`;
      }
      s = s.parent;
    }
    return name;
  }

  // 推指令
  pushInst(inst) {
    this.instList.push(inst);
  }
  // 推数据
  push_big_str(val) {
    let indexOfVal = this.poolList.indexOf(val);
    if (indexOfVal === -1) {
      this.poolList.push(val);

      this.pushInst(INST.PUSH);
      this.pushInst(this.poolList.length - 1);
    } else {
      this.pushInst(INST.PUSH);
      this.pushInst(indexOfVal);
    }
  }
  // 递归编译函数
  complieStatement(node) {
    switch (node.type) {
      // 作用域 变量操作(生命 获取)    获取变量
      case "Identifier": {
        let node_id = node;
        let scopeName = this.toscopeName(node_id);
        this.push_big_str(scopeName);
        this.pushInst(INST.LAOD);
        break;
      }
      // 作用域  变量操作(生命 获取)     生命变量  块级作用域变量名重命名
      case "VariableDeclarator":
        let { id, init } = node;
        // 这里说白了就是把某个作用域下的变量名入栈 具体的值(可能有值也可能是undefined指令)入栈  最后入栈一个store指令
        let scopeName = this.toscopeName(id);
        this.push_big_str(scopeName);
        if (init != null) {
          this.complieStatement(init);
        } else {
          this.pushInst(INST.undefine);
        }
        this.pushInst(INST.STORE);
        break;

      case "VariableDeclaration":
        // 作用域问题处理一下 率先进行无脑大胆的进行变量声明  bindings已经解决了作用域问题
        let { bindings, uid } = node.scope;
        for (const key in bindings) {
          this.push_big_str(`zq${uid}_${key}`);
          this.pushInst(INST.DEF);
        }

        let { declarations } = node;
        for (let i = 0; i < declarations.length; i++) {
          this.complieStatement(declarations[i]);
        }
        break;

      // 其他一些demo编译
      case "NumericLiteral":
        let { value } = node;
        this.push_big_str(value);
        break;
      case "BinaryExpression":
        let { left, right, operator } = node;
        this.complieStatement(left);
        this.complieStatement(right);

        switch (operator) {
          case "+":
            this.pushInst(INST.ADD);
            break;
          default:
            throw new Error("编译器--未实现的运算符: " + operator);
        }
        break;
      case "ExpressionStatement":
        let { expression } = node;
        this.complieStatement(expression);
        break;
      case "BlockStatement":
      case "Program":
        let { body } = node;
        for (let i = 0; i < body.length; i++) {
          this.complieStatement(body[i]);
        }
        break;
      default:
        throw new Error("编译器--未实现的语句: " + node.type);
    }
  }

  compile() {
    // 标记作用域层级  双向绑定到node上 为了拿到当前变量属于那个作用域
    traverse(this.ast, {
      enter(path) {
        let { scope, node } = path;
        node.scope = scope;
      },
    });

    // 开始实际编译
    this.complieStatement(this.ast.program);
  }
}
// 作用域对象
function Scope(parentScope) {
  this.data = {};
  if (parentScope) {
    this.data.__proto__ = parentScope.data;
  } else {
    this.data.__proto__ = globalThis;
  }
}

Scope.prototype.def = function (name) {
  // 直接定义
  this.data[name] = undefined;
};

Scope.prototype.store = function (name, value) {
  // 这里必须要从原型链上一步步找到这个变量
  let data = this.data;
  while (!data.hasOwnProperty(name) && data !== globalThis) {
    data = data.__proto__;
  }
  data[name] = value;
};
Scope.prototype.load = function (name) {
  // 这里必须要从原型链上一步步找到这个变量 已经开始找了，所以不用再判断了  this.data.__proto__ 这个就是官方实现的机制
  return this.data[name];
};

// 解释器
function vmFunc(instlist, poolList) {
  // 必须借助一个栈
  var stack = [];
  // 当前运行的指令索引
  var pc = 0;
  // 作用域对象
  var scope = new Scope();

  while (true) {
    var inst = instlist[pc++];

    switch (inst) {
      case INST.DEF:
        {
          let key = stack.pop();
          scope.def(key);
        }
        break;
      //作用域变量操作 块级作用域变量名重命名
      case INST.STORE:
        {
          let value = stack.pop();
          let name = stack.pop();
          scope.store(name, value);
          stack.push(value);
        }
        break;
      case INST.undefine:
        stack.push(undefined);
        break;
      case INST.LAOD: {
        let name = stack.pop();
        let value = scope.load(name);
        stack.push(value);
        break;
      }

      case INST.PUSH:
        let indexof_pool = instlist[pc++];
        stack.push(poolList[indexof_pool]);
        break;
      case INST.ADD:
        let right = stack.pop();
        let left = stack.pop();
        stack.push(right + left);
        break;
      default:
        console.log(stack);
        throw new Error("解释器-未实现的指令: " + INST[inst]);
    }
  }
}

function main() {
  const code = fs.readFileSync(
    "./p1_005_作用域对象_变量操作_块级变量名重命名_input.js",
    "utf-8"
  );

  const compiler = new Complier(code);
  compiler.compile();
  console.log("================常量表=====================");
  console.log(compiler.poolList);
  console.log("================指令表=====================");
  console.log(compiler.instList);
  vmFunc(compiler.instList, compiler.poolList);
}

main();
