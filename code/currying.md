```js
function sum(...args) {
    const res = args.reduce((a, b) => a + b, 0);  // sum of arguments
    const myFunc = (num) => {
        return sum(num, ...args);  // recursive call
    }
    myFunc.value = res;  // store current sum result as a property
    return myFunc;       // return the function
}


console.log(sum(4, 6, 8, 10).value) o/p: 28
console.log(sum(4)(6)(8)(10).value) o/p: 28
```
Key points:

...args
Collects all arguments into an array.

res
Adds all the arguments using reduce.
Example: sum(4, 6, 8, 10) → res = 28.

myFunc

Is itself a function that accepts one number (num).

Calls sum(num, ...args) again (recursively), but with the new number prepended to the old arguments.

This makes it possible to keep chaining calls like sum(4)(6)(8)(10).

myFunc.value
Attaches the total sum (res) to the returned function object.
So when you do .value, you get the result at that stage.

First case:
console.log(sum(4, 6, 8, 10).value)


args = [4, 6, 8, 10]

res = 28

.value = 28
✅ Output: 28

Second case:
console.log(sum(4)(6)(8)(10).value)


Let’s expand step by step:

sum(4)

args = [4], res = 4

Returns myFunc with .value = 4.

Call (6) → i.e. myFunc(6)

Executes return sum(6, ...args)

That means sum(6, 4)

args = [6, 4], res = 10

Returns myFunc with .value = 10.

Call (8) → sum(8, 6, 4)

res = 18

Returns function with .value = 18.

Call (10) → sum(10, 8, 6, 4)

res = 28

Returns function with .value = 28.

✅ Output: 28

In short:

sum(4,6,8,10).value → directly sums in one go.

sum(4)(6)(8)(10).value → builds the sum step by step through function chaining.

Both give the same result 28 🎯
