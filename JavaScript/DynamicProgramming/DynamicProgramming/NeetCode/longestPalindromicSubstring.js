/*
Longest Palindromic Substring
Given a string s, return the longest substring of s that is a palindrome.

A palindrome is a string that reads the same forward and backward.

If there are multiple palindromic substrings that have the same length, return any one of them.

Example 1:

Input: s = "ababd"

Output: "bab"
Explanation: Both "aba" and "bab" are valid answers.

Example 2:

Input: s = "abbc"

Output: "bb"
Constraints:

1 <= s.length <= 1000
s contains only digits and English letters.
*/

// BRUTE FORCE
const bruteLongestPalindrome = (s) => {
  let letters = "";
  let result = "";

  for (let letter of s) {
    letters = letter + letters;
    if (letters.split("").reverse().join("") === letters) {
      result = letters;
    }
    let palindrome = bruteLongestPalindrome(s.slice(letter.length));
    if (result.length < palindrome.length) {
      result = palindrome;
    }
  }
  return result;
};

console.log(bruteLongestPalindrome(""));
console.log(bruteLongestPalindrome("a"));
console.log(bruteLongestPalindrome("ababd")); // "aba"
console.log(bruteLongestPalindrome("abaaaab"));
console.log(bruteLongestPalindrome("abbc")); // "bb"
console.log(bruteLongestPalindrome("aacabdkacaa")); // aca, not efficient

// MEMOIZATION
const memoLongestPalindrome = (s, memo = {}) => {
  if (s === "") return "";
  //   if (s in memo) return memo[s];
  let result = "";
  let letters = "";

  for (let letter of s) {
    letters = letter + letters;
    if (letters.split("").reverse().join("") === letters) {
      result = letters;
    }

    let palindrome = bruteLongestPalindrome(s.slice(result.length), memo);
    if (result.length < palindrome.length) {
      result = palindrome;
    }
  }
  memo[s] = result;
  return result;
};

// console.log(memoLongestPalindrome(""));
// console.log(memoLongestPalindrome("a"));
// console.log(memoLongestPalindrome("ababd")); // "aba"
// console.log(memoLongestPalindrome("abaaaab"));
// console.log(memoLongestPalindrome("abbc")); // "bb"
// console.log(memoLongestPalindrome("aacabdkacaa")); // aca

const tabLongestPalindrome = (s) => {
    const table = Array(s.length + 1).fill(null)
    table[0] = ''

    for (let i = 0; i <= s.length; i++) {

    }
};
