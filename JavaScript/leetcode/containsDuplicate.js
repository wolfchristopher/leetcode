// LEETCODE: 217. Contains Duplicate

// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

// Example 1:

// Input: nums = [1,2,3,1]
// Output: true
// Example 2:

// Input: nums = [1,2,3,4]
// Output: false
// Example 3:

// Input: nums = [1,1,1,3,3,4,3,2,4,2]
// Output: true
 

// Constraints:

// 1 <= nums.length <= 105
// -109 <= nums[i] <= 109


/*
MY NOTES:
    It ia easy to check for duplicates of an array by putting the items of the 
    array in a HashSet. You first check if the value is in the set already and if
    it is not in the HashSet add it into the set, if it checks and sees that the
    value is already in the set the return true. If it goes through the entire
    array with no duplicates return false.

    By Doing this you will get a time complexity of O(n)
*/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const seenValues = new Set();

    for (let value of nums) {
        if (seenValues.has(value)) {
            return true;
        }
        seenValues.add(value);
    }

    return false;
};

// O(n)
