"""
23. merge k sorted lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.

"""
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge_two_lists(l1, l2): # This defines a helper function that will merge two individual sorted linked lists, l1 and l2. This function is crucial for merging lists pairwise in the divide-and-conquer approach.
            dummy = ListNode(0) # We create a dummy node to simplify the merging process. The dummy node is used as a placeholder to build the merged list. The actual merged list will start from dummy.next. Using a dummy node avoids handling special cases (like an empty list) during the merge process.
            current = dummy # We initialize the current pointer to the dummy node. The current pointer will be used to traverse and build the merged list.
            while l1 and l2: # This loop iterates as long as both l1 and l2 have nodes to process. It will stop when at least one of the lists is exhausted.
                if l1.val < l2.val: # This checks which of the two lists (l1 or l2) has the smaller value at its head. We are merging them in ascending order, so we always want to add the smaller value first.
                    current.next = l1 # If l1.val is smaller, we append the current node of l1 to the merged list by setting current.next to l1.
                    l1 = l1.next # After appending l1 to the merged list, we move the l1 pointer to the next node.
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            current.next = l1 if l1 else l2
            return dummy.next

        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(merge_two_lists(l1, l2))
            lists = merged_lists

        return lists[0]

mergeKLists([[1,4,5],[1,3,4],[2,6]])
mergeKLists([])
mergeKLists([[]])