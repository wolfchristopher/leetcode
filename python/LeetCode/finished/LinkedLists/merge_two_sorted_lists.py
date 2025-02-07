# 21. Merge Two Sorted Lists
# Easy
#
# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
# Example 1:
#
# Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
# Output: [1, 1, 2, 3, 4, 4]
#
# Example 2:
#
# Input: list1 = [], list2 = []
# Output: []
#
# Example 3:
#
# Input: list1 = [], list2 = [0]
# Output: [0]
#
# Constraints:
#
# The number of nodes in both lists is in the range[0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non - decreasing order.

from typing import Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode() # Create a Dummy Node, so you do not have to worry about inserting into an empty list.
    tail = dummy # Tail of our list is initially the dummy. The tail variable and not dummy variable is used to move through and populate the dummy linked list.
    # if I used dummy variable only it would have the list at the end for the return because the memory address is pointing towards the end of the linked list and not the beginniing.
    # This creates an issue on submission. So I create a tail variable to populate and then return the populated dummy.

    # Now I need to iterate through the two lists.
    while list1 and list2:  # You need to establish a condition and that condition will be if both of them are not empty.
        # Now I can compare the values in order to start sorting into dummy linked list.
        if list1.value <= list2.value: # if value is less than value
            tail.next = list1 # Take list1 value and insert it into the tail
            list1 = list1.next # We update our list 1 pointer to point to the next node in the linked list.
        else: # In the else condition do the same thing.
            tail.next = list2
            list2 = list2.next
        tail = tail.next # Update pointer of tail to the next node regardless of which node is used.
    # What if one of them is empty but one still has stuff inside of the list? because the conditional above does not account for this.
    if list1: # check if  there is something in list1
        tail.next = list1 # Point the remainder of list1 to the tail of the dummy list. It is already ordered so no issue.
    elif list2: # Check list2 for something in it.
        tail.next = list2 #Point the remainder of list2 to the tail.

    return dummy.next # Return the new merged and sorted linked list.

