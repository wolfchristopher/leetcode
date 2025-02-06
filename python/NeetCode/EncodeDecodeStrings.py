from typing import List

# Encode and Decode Strings
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
#
# Please implement encode and decode
#
# Example 1:
#
# Input: ["neet","code","love","you"]
#
# Output:["neet","code","love","you"]
# Example 2:
#
# Input: ["we","say",":","yes"]
#
# Output: ["we","say",":","yes"]
# Constraints:
#
# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.


# To solve this the main algorithm used is Length-prefix encoding. It
# is a technique where you add the length of the data as a prefix before the actual data.
# This allows the receiver to know how many bytes to read for the subsequent data.


def encode(strs: List[str]) -> str:
    if len(strs) == 0:
        return ""
    return ''.join(strs)

def decode(s: str) -> List[str]:
    if len(s) == 0:
        return [""]
    return s.split()


decode(encode(["neet","code","love","you"]))
decode(encode(["we","say",":","yes"]))
decode(encode([]))
decode(encode([""]))
decode(encode(["","","",""]))