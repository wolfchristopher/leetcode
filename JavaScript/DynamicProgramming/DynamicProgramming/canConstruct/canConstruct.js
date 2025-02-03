const bruteCanConstruct = (target, wordBank) => {
  if (target === "") {
    return true;
  }

  for (let word in wordBank) {
    if (target.indexOf(word) === 0) {
      const suffix = target.slice(word.length);
      if (bruteCanConstruct(suffix, wordBank) === true) {
        return true;
      }
    }
  }
  return false;
};

console.log(bruteCanConstruct("purple", ["purp", "p", "ur", "le", "purpl"])); // 2
console.log(bruteCanConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])); // 1
console.log(
  bruteCanConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
); // 0
console.log(
  bruteCanConstruct("enterapotentpot", [
    "a",
    "p",
    "ent",
    "enter",
    "ot",
    "o",
    "t",
  ])
); // 4
console.log(
  bruteCanConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee",
  ])
);

const memoizationCanConstruct = (target, wordBank, memo = {}) => {
  if (target in memo) return memo[target];
  if (target === "") return true;

  for (let word in wordBank) {
    if (target.indexOf(word) === 0) {
      const suffix = target.slice(word.length);
      if (bruteCanConstruct(suffix, wordBank, memo) === true) {
        memo[target] = true;
        return true;
      }
    }
  }
  memo[target] = false;
  return false;
};

console.log(
  memoizationCanConstruct("purple", ["purp", "p", "ur", "le", "purpl"])
); // 2
console.log(
  memoizationCanConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])
); // 1
console.log(
  memoizationCanConstruct("skateboard", [
    "bo",
    "rd",
    "ate",
    "t",
    "ska",
    "sk",
    "boar",
  ])
); // 0
console.log(
  memoizationCanConstruct("enterapotentpot", [
    "a",
    "p",
    "ent",
    "enter",
    "ot",
    "o",
    "t",
  ])
); // 4
console.log(
  memoizationCanConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee",
  ])
);
