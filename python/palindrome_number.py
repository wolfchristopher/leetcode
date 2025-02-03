# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        intString = str(x)
        if x < 0 :
            return False
        else:
            res1, res2 = split_list(intString)
            return check_palidrome(res1, res2)
def split_list(a_list):
    half = len(a_list)//2
    if len(a_list) % 2 == 0:
        return a_list[:half], a_list[half:]
    else:
        return a_list[:half], a_list[half+1:]
def check_palidrome(res1, res2):
    reversed = res2[::-1]
    if res1 == reversed:
        return True
    else:
        return False