// Classic Brute Force Fibonacci Sequence

const classic_fib = (n) => {
  if (n <= 2) return 1;
  return classic_fib(n - 1) + classic_fib(n - 2);
};

// console.log(classic_fib(6));
// console.log(classic_fib(7));
// console.log(classic_fib(8));

//Long time to Process due to O(2^n) time complexity
// console.log(classic_fib(50));

//o(n)
const foo = (n) => {
  if (n <= 1) return;
  foo(n - 1);
};

//O(2^n)
const bar = (n) => {
  if (n <= 1) return;
  bar(n - 2);
};

// memoization
// js object, keys will be the arg to the function, value will be the return value

const fib = (n, memo = {}) => {
  if (n in memo) return memo[n];
  if (n <= 2) return 1;
  memo[n] = fib(n - 1, memo) + fib(n - 2, memo);
  return memo[n];
};

console.log(fib(6));
console.log(fib(50));
