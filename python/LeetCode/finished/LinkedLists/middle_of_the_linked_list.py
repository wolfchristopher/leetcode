# 876. Middle of the Linked List
# Easy
#
# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.
#
# Example 1:
#
# Input: head = [1, 2, 3, 4, 5]
# Output: [3, 4, 5]
# Explanation: The middle node of the list is node 3.
#
# Example 2:
#
# Input: head = [1, 2, 3, 4, 5, 6]
# Output: [4, 5, 6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
#
# Constraints:
#
# The number of nodes in the list is in the range[1, 100].
# 1 <= Node.val <= 100


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Using slow and fast pointers to find the middle node.
        # This is done y making the fast pointer move two spots at a time.
        # Then setting the while condition to finish when the fast pointer reaches the end of the list.
        # During that same time the slow pointer will move a normal speed and will reach the middle
        # by the time the fast has reached the end.
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow