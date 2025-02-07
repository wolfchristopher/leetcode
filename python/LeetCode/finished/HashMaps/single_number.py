# 136. Single Number
# Easy
#
# Given a non - empty array of integers nums, every element appears twice except for one.Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.
#
# Example 1:
#
# Input: nums = [2, 2, 1]
#
# Output: 1
#
# Example 2:
#
# Input: nums = [4, 1, 2, 1, 2]
#
# Output: 4
#
# Example 3:
#
# Input: nums = [1]
#
# Output: 1
#
# Constraints:
# - 1 <= nums.length <= 3 * 104
# - -3 * 104 <= nums[i] <= 3 * 104
# - Each element in the array appears twice except for one element which appears only once.
from typing import List


def singleNumber(nums: List[int]) -> int:
    hashMap = {}
    for index, num in enumerate(nums):
        if num in hashMap:
            hashMap[num] += 1
        else:
            hashMap[num] = 1

    for key, value in hashMap.items():
        if value == 1:
            return key


print(singleNumber([2, 2, 1]))
print(singleNumber([4,1,2,1,2]))
print(singleNumber([1]))