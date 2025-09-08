JavaScript Interview Q&A – Part 5 (Coding Tasks)
## 1. Polyfill for map
<details> <summary>👉 Answer</summary>

```js
Array.prototype.myMap = function(cb) {
  let result = [];
  for (let i = 0; i < this.length; i++) {
    result.push(cb(this[i], i, this));
  }
  return result;
};

console.log([1, 2, 3].myMap(x => x * 2)); // [2, 4, 6]
```

</details>

## 2. Polyfill for filter
<details> <summary>👉 Answer</summary>

```js
Array.prototype.myFilter = function(cb) {
  let result = [];
  for (let i = 0; i < this.length; i++) {
    if (cb(this[i], i, this)) {
      result.push(this[i]);
    }
  }
  return result;
};

console.log([1, 2, 3].myFilter(x => x > 1)); // [2, 3]
```

</details>

## 3. Polyfill for reduce
<details> <summary>👉 Answer</summary>

```js
Array.prototype.myReduce = function(cb, init) {
  let acc = init !== undefined ? init : this[0];
  let start = init !== undefined ? 0 : 1;

  for (let i = start; i < this.length; i++) {
    acc = cb(acc, this[i], i, this);
  }
  return acc;
};

console.log([1, 2, 3].myReduce((a, b) => a + b, 0)); // 6
```

</details>
## 4. Flatten Array
<details> <summary>👉 Answer</summary>

```js
let arr = [1, [2, [3, [4]]]];

function flatten(array) {
  return array.reduce((acc, val) =>
    Array.isArray(val) ? acc.concat(flatten(val)) : acc.concat(val), []);
}

console.log(flatten(arr)); // [1, 2, 3, 4]
```

</details>

## 5. Flatten Object
<details> <summary>👉 Answer</summary>

```js
let obj = { a: { b: { c: 1 } } };

function flattenObject(obj, parent = "", res = {}) {
  for (let key in obj) {
    let newKey = parent ? `${parent}.${key}` : key;
    if (typeof obj[key] === "object" && obj[key] !== null) {
      flattenObject(obj[key], newKey, res);
    } else {
      res[newKey] = obj[key];
    }
  }
  return res;
}

console.log(flattenObject(obj)); // { "a.b.c": 1 }
```

</details>

## 6. Debouncing
<details> <summary>👉 Answer</summary>

```js
function debounce(fn, delay) {
  let timer;
  return function(...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

window.addEventListener("resize", debounce(() => {
  console.log("Resized!");
}, 300));
```

</details>

## 7. Throttling
<details> <summary>👉 Answer</summary>

```js
function throttle(fn, limit) {
  let last = 0;
  return function(...args) {
    let now = Date.now();
    if (now - last >= limit) {
      fn.apply(this, args);
      last = now;
    }
  };
}

window.addEventListener("scroll", throttle(() => {
  console.log("Scrolling...");
}, 500));
```

</details>

## 8. Auto Search (Search as you type)
<details> <summary>👉 Answer</summary>

```js
function search(query) {
  console.log("Searching for:", query);
}

const debouncedSearch = debounce(search, 400);

document.getElementById("search").addEventListener("input", (e) => {
  debouncedSearch(e.target.value);
});
```

</details>
## 9. Memoization
<details> <summary>👉 Answer</summary>

```js
function memoize(fn) {
  let cache = {};
  return function(...args) {
    let key = JSON.stringify(args);
    if (cache[key]) return cache[key];
    let result = fn.apply(this, args);
    cache[key] = result;
    return result;
  };
}

const slowSquare = (n) => {
  console.log("Calculating...");
  return n * n;
};

const fastSquare = memoize(slowSquare);
console.log(fastSquare(5)); // Calculating... 25
console.log(fastSquare(5)); // 25 (from cache)
```

</details>

## 10. LRU Cache
<details> <summary>👉 Answer</summary>

```js
class LRUCache {
  constructor(limit = 3) {
    this.cache = new Map();
    this.limit = limit;
  }

  get(key) {
    if (!this.cache.has(key)) return -1;
    let val = this.cache.get(key);
    this.cache.delete(key);
    this.cache.set(key, val);
    return val;
  }

  set(key, val) {
    if (this.cache.has(key)) {
      this.cache.delete(key);
    } else if (this.cache.size >= this.limit) {
      this.cache.delete(this.cache.keys().next().value);
    }
    this.cache.set(key, val);
  }
}

let lru = new LRUCache(2);
lru.set("a", 1);
lru.set("b", 2);
lru.set("c", 3); // removes "a"
console.log(lru.get("a")); // -1
```

</details>

## 11. Retry Logic
<details> <summary>👉 Answer</summary>

```js
function fetchWithRetry(fn, retries = 3, delay = 1000) {
  return new Promise((resolve, reject) => {
    fn()
      .then(resolve)
      .catch((err) => {
        if (retries === 0) reject(err);
        else setTimeout(() => {
          fetchWithRetry(fn, retries - 1, delay).then(resolve, reject);
        }, delay);
      });
  });
}
```

</details>

## 12. Deep Clone
<details> <summary>👉 Answer</summary>

```js
function deepClone(obj) {
  return JSON.parse(JSON.stringify(obj));
}

let obj = { a: 1, b: { c: 2 } };
let clone = deepClone(obj);
clone.b.c = 5;
console.log(obj.b.c); // 2
```

</details>

## 13. Object Compare
<details> <summary>👉 Answer</summary>

```js
function isEqual(obj1, obj2) {
  return JSON.stringify(obj1) === JSON.stringify(obj2);
}

console.log(isEqual({ a: 1 }, { a: 1 })); // true
```

</details>

## 14. Object Sort
<details> <summary>👉 Answer</summary>

```js
let arr = [{ age: 30 }, { age: 20 }, { age: 40 }];
arr.sort((a, b) => a.age - b.age);
console.log(arr); // [{20}, {30}, {40}]
```

</details>

## 15. Promise with async/await
<details> <summary>👉 Answer</summary>

```js
function delay(ms) {
  return new Promise((res) => setTimeout(res, ms));
}

async function run() {
  await delay(1000);
  console.log("1 second later");
}
run();
```

</details>

## 16. Counter Reset
<details> <summary>👉 Answer</summary>

```js
function counter() {
  let count = 0;
  return {
    inc: () => ++count,
    reset: () => count = 0
  };
}

let c = counter();
console.log(c.inc()); // 1
console.log(c.inc()); // 2
c.reset();
console.log(c.inc()); // 1
```

</details>

## 17. Timers in JavaScript
<details> <summary>👉 Answer</summary>

```js
setTimeout(() => console.log("Once after 1s"), 1000);

let id = setInterval(() => console.log("Every 2s"), 2000);
setTimeout(() => clearInterval(id), 7000); // stop after 7s
```

</details>

## 18. Object Sum
<details> <summary>👉 Answer</summary>

```js
let arr = [{ a: 1 }, { a: 2 }, { a: 3 }];
let total = arr.reduce((sum, obj) => sum + obj.a, 0);
console.log(total); // 6
```

</details>
