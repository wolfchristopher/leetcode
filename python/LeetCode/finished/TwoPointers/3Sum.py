"""
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

Efficient Approach: Two-Pointer Technique
- Sort the array: This helps avoid duplicates and allows for efficient two-pointer traversal.
- Fix one element (nums[i]), then use two pointers (left and right) to find the other two elements.
- Move pointers smartly to avoid duplicates.

Time Complexity
- Sorting: O(n log n)
- Two-pointer traversal: O(n^2) (each number is fixed once, and the remaining two are found in O(n))
- Overall Complexity: O(n^2), which is optimal for this problem.

Why This Works?
- Sorting helps eliminate duplicates efficiently
- Two-pointer strategy ensures we efficiently find triplets
- Duplicate checks prevent adding the same triplet multiple times
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate elements
                continue

            left, right = i + 1, len(nums) - 1  # Two-pointer approach
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicate values for left and right
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:  # Need a larger sum, move left pointer right
                    left += 1
                else:  # Need a smaller sum, move right pointer left
                    right -= 1

        return res