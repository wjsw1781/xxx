
const fs=require('fs');

const parser=require('@babel/parser');
const traverse=require('@babel/traverse').default;
const generate=require('@babel/generator').default;



class Complier{
    constructor(code){
        this.ast=parser.parse(code);
        // 指令表
        this.instList=[];
        // 常量表
        this.poolList=[]
    }
    complie_statement(node){
        switch (node.type) {
            case 'ExpressionStatement':
                this.compile_expression(node.expression);
                this.instList.push(4);
                break;
            default:
                throw new Error("未实现的语句: " + node.type);
        }
    }

    compile(){
        this.complie_statement(this.ast.program)
    }

}


function vmFunc(instlist,poolList) {
    // 必须借助一个栈
    var stack = [];
    // 当前运行的指令索引
    var pc = 0;

    // 一些常量
    let right ;
    let left ;

    // 逐条执行指令
    while (true) {
        var inst = instlist[pc++];


        switch (inst) {
            case 1:
                stack.push(instlist[pc++]);
                break;
            case 2:
                right = stack.pop();
                left = stack.pop();
                stack.push(right * left);
                break;
            case 3:
                right = stack.pop();
                left = stack.pop();
                stack.push(right + left);
                break;
            case 4:
                console.log(stack.pop());
                break;
            default:
                throw new Error("未实现的指令: " + inst);
        }
    }
}

function main(){
    const code=fs.readFileSync('./p1_003_搭建基本框架_input.js','utf-8');

    const compiler=new Complier(code);
    compiler.compile();

    vmFunc(compiler.instList,compiler.poolList)

}

main();



