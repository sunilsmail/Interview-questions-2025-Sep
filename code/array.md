```js

function insertAt(arr, index, value) {
    for (let i = arr.length; i > index; i--) {
        arr[i] = arr[i - 1];
    }
    arr[index] = value;
}

const array = [1, 2, 4, 5];
insertAt(array, 2, 3)
console.log(array)
o/p: [1, 2, 3, 4, 5]

function removeAt(arr, index) {
    for (let i = index; i < arr.length - 1; i++) {
        arr[i] = arr[i + 1]; // shift elements left
    }
    arr.length--; // shrink the array
}

const array1 = [1, 2, 2, 4, 5];
removeAt(array1, 2)
console.log(array1)
o/p: [1, 2, 4, 5]

```
