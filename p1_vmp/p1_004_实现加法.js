
const fs=require('fs');

const parser=require('@babel/parser');
const traverse=require('@babel/traverse').default;
const generate=require('@babel/generator').default;

const INST={} ;{
    INST[INST['ADD']=1] = 'ADD';



    INST[INST['PUSH']=101] = 'PUSH';
}
class Complier{
    constructor(code){
        this.ast=parser.parse(code);
        // 指令表
        this.instList=[];
        // 常量表
        this.poolList=[]
    }
    pushInst(inst){
        this.instList.push(inst);
    }
    // 生成指令+数据 就是推到大字符串 : 先推push指令 然后推常量索引
    push_big_str(val){
        let indexOfVal=this.poolList.indexOf(val);
        if (indexOfVal===-1){
            this.poolList.push(val);

            this.pushInst(INST.PUSH);
            this.pushInst(this.poolList.length-1);
        } else {
            this.pushInst(INST.PUSH);
            this.pushInst(indexOfVal);
        }
    }
    complie_statement(node){
        switch (node.type) {
            case 'NumericLiteral':
                let {value}=node;
                this.push_big_str(value);
                break;
            case 'BinaryExpression':
                let {left,right,operator}=node;
                this.complie_statement(left);
                this.complie_statement(right);

                switch (operator) {
                    case '+':
                        this.pushInst(INST.ADD);
                        break;
                    default:
                        throw new Error("编译器--未实现的运算符: " + operator);
                }
                break;
            case 'ExpressionStatement':
                let {expression}=node;
                this.complie_statement(expression);
                break;
            case 'Program':
                let {body}=node;
                for (let i = 0; i < body.length; i++) {
                    this.complie_statement(body[i]);
                }
                break
            default:
                throw new Error("编译器--未实现的语句: " + node.type);
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
    // 逐条执行指令
    while (true) {
        var inst = instlist[pc++];


        switch (inst) {
            case INST.PUSH:
                let indexof_pool = instlist[pc++];
                stack.push(poolList[indexof_pool]);
                break;
            case INST.ADD:
                let right = stack.pop();
                let left = stack.pop();
                stack.push(right +left);
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
                console.log(stack)
                throw new Error("解释器-未实现的指令: " + INST[inst]);
        }
    }
}

function main(){
    const code=fs.readFileSync('./p1_004_实现加法_input.js','utf-8');

    const compiler=new Complier(code);
    compiler.compile();
    console.log("================常量表=====================")
    console.log(compiler.poolList)
    console.log("================指令表=====================")
    console.log(compiler.instList)
    vmFunc(compiler.instList,compiler.poolList)

}

main();



