const bruteCanSum = (targetSum, numbers) => {
  if (targetSum === 0) return true;
  if (targetSum < 0) return false;

  for (let num of numbers) {
    const remainder = targetSum - num;
    if (bruteCanSum(remainder, numbers) === true) {
      return true;
    }
  }

  return false;
};
console.log("#######-BRUTE-FORCE-#######");
console.log(bruteCanSum(7, [2, 3])); // True
console.log(bruteCanSum(7, [5, 3, 4, 7])); // True
console.log(bruteCanSum(7, [2, 4])); // False
console.log(bruteCanSum(7, [5, 3, 2])); // True

// console.log(bruteCanSum(300, [7, 14])); // False, not efficient

const canSum = (targetSum, numbers, memo = {}) => {
  if (targetSum in memo) return memo[targetSum];
  if (targetSum === 0) return true;
  if (targetSum < 0) return false;

  for (let num of numbers) {
    const remainder = targetSum - num;
    if (bruteCanSum(remainder, numbers, memo) === true) {
      memo[targetSum] = true;
      return true;
    }
  }
  memo[targetSum] = false;
  return false;
};
console.log("#######-MEMOIZATION-#######");
console.log(canSum(7, [2, 3])); // True
console.log(canSum(7, [5, 3, 4, 7])); // True
console.log(canSum(7, [2, 4])); // False
console.log(canSum(7, [5, 3, 2])); // True
