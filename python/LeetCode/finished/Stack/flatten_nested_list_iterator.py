"""
341. Flatten Nested List Iterator
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct.



Example 1:

Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].


Constraints:

1 <= nestedList.length <= 500
The values of the integers in the nested list is in the range [-106, 106].


Approach: Stack-Based Iteration
- A stack is the best data structure for this problem because:
- It allows LIFO (Last-In-First-Out) processing, helping us traverse nested lists.
- We push the list in reverse order so that we process elements from left to right.


How It Works
Initialization (__init__)
- Calls _flatten() to process nestedList and store elements in self.stack.
- Reverses the list before pushing to process left-to-right.

Flattening (_flatten())
- Recursively unpacks lists, pushing elements in reverse order.

Retrieving Next Element (next())
- Just pop() from self.stack (already flattened).

Checking for More Elements (hasNext())
- If the stack’s top element is an integer, return True.
- Otherwise, pop the nested list, flatten it, and continue checking.


Time Complexity
Flattening: O(N), where N is the number of integers in nestedList.

next() and hasNext(): O(1) amortized, since each element is processed once.
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self._flatten(nestedList)

    def _flatten(self, nestedList):
        """Helper function to flatten the nestedList into a stack."""
        for ni in reversed(nestedList):  # Reverse to maintain order
            self.stack.append(ni)

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]  # Peek at the top element
            if top.isInteger():
                return True  # Found an integer, return True
            self.stack.pop()  # Remove nested list from stack
            self._flatten(top.getList())  # Flatten the list
        return False