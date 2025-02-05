from itertools import islice
from typing import List

# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements within the array.
#
# The test cases are generated such that the answer is always unique.
#
# You may return the output in any order.
#
# Example 1:
#
# Input: nums = [1,2,2,3,3,3], k = 2
#
# Output: [2,3]
# Example 2:
#
# Input: nums = [7,7], k = 1
#
# Output: [7]
# Constraints:
#
# 1 <= nums.length <= 10^4.
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}
        for index, value in enumerate(nums):
            if value in numDict.keys():
                numDict[value] += 1
            else:
                numDict[value] = 1
        print(numDict)

        sorted_items = sorted(numDict.items(), key=lambda x: x[1], reverse=True)
        listNums = []
        for key in dict(sorted_items[:k]):
            listNums.append(key)

        return listNums