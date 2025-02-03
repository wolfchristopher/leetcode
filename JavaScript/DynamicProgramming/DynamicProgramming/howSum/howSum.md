#Dynamic Programming
## howSum
Write a function `howSum(targetSum, numbers)` that takes in a targetSum and an array of numbers as arguments.

The function should return an array containing any combination of elements that add up to exactly the targetSum. If there is no combination that ads up to the targetSum, then return null.

if there are multipole possible, you may return any single one.
Scenarios:
howSum(7, [5,2,3,4,7]) - [3,4]
howSum(7, [5,2,3,4,7]) - [7]
howSum(8, [2]) - []
howSum(7, [2,4]) -> null
howSum(0, [1,2,3])