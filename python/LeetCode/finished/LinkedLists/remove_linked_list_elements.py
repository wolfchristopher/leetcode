# 203. Remove Linked List Elements
# Easy
#
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val,
# and return the new head.
#
# Example 1:
#
# Input: head = [1, 2, 6, 3, 4, 5, 6], val = 6
# Output: [1, 2, 3, 4, 5]
#
# Example 2:
#
# Input: head = [], val = 1
# Output: []
#
# Example 3:
#
# Input: head = [7, 7, 7, 7], val = 7
# Output: []
#
# Constraints:
# - The number of nodes in the list is in the range[0, 104].
# - 1 <= Node.val <= 50
# - 0 <= val <= 50

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode(0)  # Dummy node before head
    dummy.next = head # Sets the initial dummy node to {None -> head} head has all of the rest of the nodes.
    current = dummy  # Pointer to traverse

    while current.next:  # Iterate through the list
        if current.next.val == val:
            current.next = current.next.next  # Skip the node
        else:
            current = current.next  # Move forward

    return dummy.next  # Return the new head and ignoring None first value.