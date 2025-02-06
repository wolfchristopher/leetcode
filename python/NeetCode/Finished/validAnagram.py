
# My First attempt used sorted() to arrange strings to check equality
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one = sorted(s)
        two = sorted(t)
        if one == two:
            return True
        return False

isAnagram = Solution().isAnagram("yay", "ayy")