# 206. Reverse Linked List
# Easy
#
# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
# Example 1:
#
# Input: head = [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
#
# Example 2:
#
# Input: head = [1, 2]
# Output: [2, 1]
#
# Example 3:
#
# Input: head = []
# Output: []
#
# Constraints:
#
# The number of nodes in the list is the range[0, 5000].
# -5000 <= Node.val <= 5000

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Reverse a singly linked list using pointer manipulation (iterative or recursive).
class Solutions:
    def iterativeReverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:  #Optional[ListNode] means the function can accept or return None (empty list).
        curr = head # curr starts at the head (beginning of the list).
        prev = None # prev is initialized as None because the last node will point to None after reversal.

        # Traverse all the nodes of Linked List
        while curr is not None: # Loop runs until we reach the end of the linked list (curr becomes None).

            # Store next
            nextNode = curr.next # Since we are going to modify curr.next, we store a reference to the next node.

            # Reverse current node's next pointer
            curr.next = prev # The reversal happens here: Instead of pointing to the next node, curr.next now points backward to prev

            # Move pointers one position ahead
            prev = curr # Move prev one step forward (to the current node).
            curr = nextNode # Move curr one step forward (to the stored nextNode).

        # Return the head of reversed linked list
        return prev # When curr becomes None, prev is at the new head of the reversed linked list

    def recursiveReverseList(head):
        if head is None or head.next is None:
            return head

        # reverse the rest of linked list and put the
        # first element at the end
        rest = head.recursiveReverseList(head.next)

        # Make the current head as last node of
        # remaining linked list
        head.next.next = head

        # Update next of current head to NULL
        head.next = None

        # Return the reversed linked list
        return rest