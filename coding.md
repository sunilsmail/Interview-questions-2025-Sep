```js
function sum(...args) {
    const res = args.reduce( (a, b) => a + b, 0);
    const myFunc = (num) => {
        return sum(num, ...args);
    }
    myFunc.value = res;
    return myFunc;
}

console.log(sum(4, 6, 8, 10).value)
console.log(sum(4)(6)(8)(10).value)
```
