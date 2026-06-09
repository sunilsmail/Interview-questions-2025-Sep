function subsets(nums) {
    let result = [];
    let currentSubset = [];

    function backtrack(index) {
        // BASE CASE: If we ran out of numbers, save our basket and stop
        if (index === nums.length) {
            // We slice() to make a fresh copy, otherwise future changes ruin it
            result.push(currentSubset.slice()); 
            return;
        }

        // CHOICE 1: INCLUDE the current number
        currentSubset.push(nums[index]); // Choose
        backtrack(index + 1);            // Explore

        // THE BACKTRACK STEP: Take it out
        currentSubset.pop();             // Un-choose

        // CHOICE 2: EXCLUDE the current number
        backtrack(index + 1);            // Explore
    }

    // Start the process at the very first number (index 0)
    backtrack(0); 
    return result;
}

// Example usage:
console.log(subsets([1, 2, 3]));
