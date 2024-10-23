 function vmFunc(instlist) {
    // 必须借助一个栈
    var stack = [];
    // 当前运行的指令索引
    var pc = 0;
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

console.log(2*5+8)
// 指令含义映射
// PUSH               1
// multiply           2
// add                3
// console.log        4
let human_complier_inslist=[1,2,1,5,2,1,8,3,4]
vmFunc(human_complier_inslist)

