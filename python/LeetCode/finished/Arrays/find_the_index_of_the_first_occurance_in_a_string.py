class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)  # Built in find method can check a string for a substring. O(n), O(1) space