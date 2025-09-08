# JavaScript Concepts – Interview Q&A

---

## 1. null vs undefined
<details><summary>👉 Answer</summary>

- **null** → Intentional absence of value (assigned by developer).  
- **undefined** → Default value of uninitialized variables.  

```js
let a;
console.log(a); // undefined

let b = null;
console.log(b); // null
```
</details>

## 2. indexOf vs findIndex
<details><summary>👉 Answer</summary>
indexOf → Works on primitive values, returns index or -1.

findIndex → Uses callback, works with objects/conditions.

```js

const arr = [10, 20, 30];

console.log(arr.indexOf(20)); // 1
console.log(arr.findIndex(x => x > 15)); // 1
```

</details>
## 3. slice vs splice
<details><summary>👉 Answer</summary>
slice(start, end) → Returns shallow copy, does not modify original.

splice(start, deleteCount, ...items) → Modifies original array.

```js

const arr = [1, 2, 3, 4];

console.log(arr.slice(1, 3)); // [2,3]
console.log(arr);             // [1,2,3,4]

console.log(arr.splice(1, 2)); // [2,3]
console.log(arr);              // [1,4]
```

</details>
## 4. find vs filter
<details><summary>👉 Answer</summary>
find → Returns first matching element.

filter → Returns all matching elements (array).


```js
const nums = [5, 10, 15, 20];

console.log(nums.find(n => n > 10));   // 15
console.log(nums.filter(n => n > 10)); // [15,20]
```

</details>
## 5. setTimeout vs setInterval
<details><summary>👉 Answer</summary>
setTimeout → Runs once after delay.

setInterval → Runs repeatedly with delay interval.

```js

setTimeout(() => console.log("Runs once"), 1000);

setInterval(() => console.log("Runs every second"), 1000);
```

</details>
## 6. Object.create() vs Constructor Functions
<details><summary>👉 Answer</summary>
Object.create(proto) → Creates new object with prototype.

Constructor Function → Uses new keyword to create objects.

```js

// Object.create
const proto = { greet() { console.log("Hello"); } };
const obj = Object.create(proto);
obj.greet(); // Hello

// Constructor function
function Person(name) { this.name = name; }
Person.prototype.say = function() { console.log(this.name); };
const p = new Person("John");
p.say(); // John
```
</details>
## 7. Function Expression vs Function Declaration
<details><summary>👉 Answer</summary>
Declaration → Hoisted, can be used before definition.

Expression → Not hoisted, assigned to variable.

```js

sayHi(); // works
function sayHi() { console.log("Hi"); }

// sayHello(); // Error
const sayHello = function() { console.log("Hello"); };
```
</details>
## 8. Debouncing vs Throttling
<details><summary>👉 Answer</summary>
Debounce → Run function only after certain delay without new calls.

Throttle → Run function at fixed interval, ignoring extra calls.


```js
// Debounce (e.g., search input)
function debounce(fn, delay) {
  let timer;
  return function(...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}

// Throttle (e.g., scroll)
function throttle(fn, delay) {
  let last = 0;
  return function(...args) {
    let now = Date.now();
    if (now - last >= delay) {
      fn(...args);
      last = now;
    }
  };
}
```
</details>
## 9. Arrow vs Normal Functions
<details><summary>👉 Answer</summary>
Arrow → No this, no arguments, shorter syntax.

Normal → Has own this & arguments.

```js

const obj = {
  normal() { console.log(this); }, // obj
  arrow: () => console.log(this),  // window/global
};

obj.normal();
obj.arrow();
</details>
## 10. call vs apply vs bind
<details><summary>👉 Answer</summary>
call → Calls function with this, args comma-separated.

apply → Calls function with this, args as array.

bind → Returns new function with bound this.



function greet(msg) { console.log(msg, this.name); }
const person = { name: "Alice" };

greet.call(person, "Hello");       // Hello Alice
greet.apply(person, ["Hi"]);       // Hi Alice
const fn = greet.bind(person);
fn("Hey");                         // Hey Alice
```

</details>

## 11. let vs const vs var
<details><summary>👉 Answer</summary>
var → Function scope, hoisted.

let → Block scope, no redeclare.

const → Block scope, must initialize, no reassignment.

```js

var x = 1;
let y = 2;
const z = 3;
</details>
## 12. map vs forEach
<details><summary>👉 Answer</summary>
map → Returns new array.

forEach → Iterates, no return.



const nums = [1, 2, 3];

console.log(nums.map(n => n * 2)); // [2,4,6]
console.log(nums.forEach(n => n * 2)); // undefined
```

</details>
## 13. pop vs shift
<details><summary>👉 Answer</summary>
pop → Removes last element.

shift → Removes first element.


```js
const arr = [1,2,3];

console.log(arr.pop());  // 3
console.log(arr.shift()); // 1
```

</details>
## 14. for-in vs for-of
<details><summary>👉 Answer</summary>
for-in → Iterates keys (including inherited).

for-of → Iterates values (iterables only).


```js
const arr = ["a","b","c"];

for (let i in arr) console.log(i);   // 0,1,2
for (let v of arr) console.log(v);   // a,b,c
```

</details>
## 15. cookie vs sessionStorage vs localStorage
<details><summary>👉 Answer</summary>
Cookie → Sent to server, small size (~4KB).

localStorage → Browser only, persists until cleared.

sessionStorage → Browser only, clears on tab close.

```js

localStorage.setItem("name", "Alice");
sessionStorage.setItem("token", "123");
document.cookie = "id=1";
```

</details>

## 16. async vs defer
<details><summary>👉 Answer</summary>
async → Loads script in parallel, executes ASAP.

defer → Loads in parallel, executes after HTML parsing.

```html

<script src="file." async></script>
<script src="file." defer></script>
```

</details>
## 17. frozen vs sealed
<details><summary>👉 Answer</summary>
Object.freeze(obj) → No add/remove/change.

Object.seal(obj) → No add/remove, but can modify existing values.

```js

const obj = { a: 1 };
Object.freeze(obj);
obj.a = 2; // ignored

const obj2 = { b: 1 };
Object.seal(obj2);
obj2.b = 2; // works
```

</details>
## 18. Shallow Copy vs Deep Copy
<details><summary>👉 Answer</summary>
Shallow Copy → Copies top-level, nested objects still reference.

Deep Copy → Full independent copy.


```js
const obj = { x: 1, y: { z: 2 } };

const shallow = { ...obj };
shallow.y.z = 99;
console.log(obj.y.z); // 99 (changed)

const deep = ON.parse(ON.stringify(obj));
deep.y.z = 100;
console.log(obj.y.z); // 99 (safe)
```

</details>
## 19. Promise.all vs any vs race vs allSettled
<details><summary>👉 Answer</summary>
all → Resolves if all succeed, rejects if one fails.

any → Resolves if one succeeds, rejects if all fail.

race → Resolves/rejects with first settled promise.

allSettled → Resolves when all complete (success/fail).

```js
Promise.all([p1, p2]);
Promise.any([p1, p2]);
Promise.race([p1, p2]);
Promise.allSettled([p1, p2]);
```
</details>
## 20. Pure vs Impure
<details><summary>👉 Answer</summary>
Pure Function → Same input → same output, no side effects.

Impure Function → Depends on external state or has side effects.

```js
// Pure
function add(a,b){ return a+b; }

// Impure
let x = 1;
function addToX(y){ return x+y; }
```
</details>
