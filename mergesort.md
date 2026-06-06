function mergeSort(arr) {
  // BASE CASE: An array of 0 or 1 item is already sorted!
  if (arr.length <= 1) return arr;

  // Split the array down the middle
  const middle = Math.floor(arr.length / 2);
  const leftHalf = arr.slice(0, middle);
  const rightHalf = arr.slice(middle);

  // RECURSIVE CALL: Tell the function to split and sort both halves
  return merge(mergeSort(leftHalf), mergeSort(rightHalf));
}

// Helper function to zip two sorted arrays together
function merge(left, right) {
  let result = [];
  while (left.length && right.length) {
    if (left[0] < right[0]) result.push(left.shift());
    else result.push(right.shift());
  }
  return [...result, ...left, ...right];
}

console.log(mergeSort([4, 2, 1, 3])); // Output: [1, 2, 3, 4]
