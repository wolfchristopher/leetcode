# Given
# an
# integer
# array
# nums,
# return true if any
# value
# appears
# at
# least
# twice in the
# array, and return false if every
# element is distinct.
#
# Example
# 1:
#
# Input: nums = [1, 2, 3, 1]
#
# Output: true
#
# Explanation:
#
# The
# element
# 1
# occurs
# at
# the
# indices
# 0 and 3.
#
# Example
# 2:
#
# Input: nums = [1, 2, 3, 4]
#
# Output: false
#
# Explanation:
#
# All
# elements
# are
# distinct.
#
# Example
# 3:
#
# Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
#
# Output: true
#
# Constraints:
#
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
from typing import List


# I used a Hash map to optimize.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for index, num in enumerate(nums):
            if num in my_dict.keys():
                return True
            else:
                my_dict[num] = index

        return False


## My Brute force solution
class BruteSolution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for index, num in enumerate(nums):
            for index1, num1 in enumerate(nums):
                if num == num1 and not index == index1:
                    return True
        return False



# Other solutions are Sorting, Hash Set and Hash Set Length
# Need to learn those other methods.

class SortingSolution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for index, num in enumerate(nums):
            if num == nums[index - 1] and not index == 0:
                return True

        return False
