/* eslint-disable no-prototype-builtins */

// 模拟作用域对象机制
function Scope(parentScope) {
  this.data = {};
  if (parentScope) {
    this.data.__proto__ = parentScope.data;
  } else {
    this.data.__proto__ = globalThis;
  }
}

Scope.prototype.def = function (name, value) {
    // 直接定义
    this.data[name] = value;
}

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



let scope1=new Scope()
let scope2=new Scope(scope1)
scope2.store('a', 100)
console.log(scope1.load('a'))
console.log(a)

// ff=100
// current_scope.define('fff', 200)

// console.log(current_scope.load('fff'))
// console.log(current_scope.load('ff'))
