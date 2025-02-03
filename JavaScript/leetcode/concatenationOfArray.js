/*
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

 

Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
 

Constraints:

n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 1000

*/

let getConcatenation = (nums) => {
  let nums2 = nums.slice(); // OR use spread Operator [...nums]
  for (let num of nums) {
    nums2.push(num);
  }
  return nums2;
};

console.log(getConcatenation([1, 2, 1]));


/* 
The .slice() method in JavaScript is used to create a shallow copy of a portion of an array into a new 
array object selected from start to end (end not included). The original array will not be modified.
        
        array.slice([start[, end]])

    - start: Optional. An integer that specifies where to start the selection. If omitted, the slice begins from index 0. 
            If negative, it specifies the index from the end of the array.
    - end: Optional. An integer that specifies where to end the selection (end not included). If omitted, 
            the slice includes all elements from the start to the end of the array. If negative, it specifies the index 
            from the end of the array.
Examples:
Basic Usage
        let array = [1, 2, 3, 4, 5];
        let newArray = array.slice(1, 3);
        console.log(newArray); // Output: [2, 3]


*/
