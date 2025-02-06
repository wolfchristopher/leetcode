# 771. Jewels and Stones
#
# Easy
#
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
#
# Letters are case sensitive, so "a" is considered a different type of stone from "A".
#
# Example 1:
#
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
#
# Example 2:
#
# Input: jewels = "z", stones = "ZZ"
# Output: 0
#
# Constraints:
#
# 1 <= jewels.length, stones.length <= 50
# jewels and stones consist of only English letters.
# All the characters of jewels are unique.

def numJewelsInStones(jewels: str, stones: str) -> int:
    jewelList = list(jewels)
    stoneList = list(stones)
    jewelHash = {}

    for index, value in enumerate(jewelList):
        if value in jewelHash:
            jewelHash[value] += 1
        else:
            jewelHash[value] = 1
    total = int()
    for index, value in enumerate(stoneList):
        if value in jewelHash:
            total += 1
    return total

print(numJewelsInStones(jewels="aA", stones="sAAbbbb"))
print(numJewelsInStones(jewels="z", stones="ZZ"))