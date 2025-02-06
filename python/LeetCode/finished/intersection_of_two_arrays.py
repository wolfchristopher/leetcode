# 349. Intersection of Two Arrays
# Easy
#
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.
#
# Example 1:
#
# Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# Output: [2]
#
# Example 2:
#
# Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
# Output: [9, 4]
# Explanation: [4, 9] is also accepted.
#
# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
from typing import List


def intersection( nums1: List[int], nums2: List[int]) -> List[int]:
    hashMap1 = {}
    hashMap2 = {}
    for index, value in enumerate(nums1):
        if value in hashMap1:
            hashMap1[value] += 1
        else:
            hashMap1[value] = 1

    for index, value in enumerate(nums2):
        if value in hashMap2:
            hashMap2[value] += 1
        else:
            hashMap2[value] = 1

    retList = []
    for key, value in enumerate(hashMap1):
        if value in hashMap2:
            retList.append(value)

    return retList

print(intersection([1,2,3,4], [1,3,4]))
print(intersection([1,2,2,1], [2,2]))
print(intersection([4,9,5], [9,4,9,8,4]))