# 83. Remove Duplicates from Sorted List
# Easy
#
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.Return the linked list sorted as well.
#
# Example 1:
#
# Input: head = [1, 1, 2]
# Output: [1, 2]
#
# Example 2:
#
# Input: head = [1, 1, 2, 3, 3]
# Output: [1, 2, 3]
#
# Constraints:
#
# The number of nodes in the list is in the range[0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head  # Use a pointer to traverse the list

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # Skip duplicate node
            else:
                current = current.next

        return head

# Convert Binary Number in a Linked List to Integer (LC 1290)
#
# Traverse the linked list and compute the binary number as an integer using bitwise operations.
# Odd Even Linked List (LC 328)
