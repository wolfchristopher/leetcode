// var longestCommonPrefix = function (strs) {
//   let letters = [];
//   let shortestWord = [];
//   let firstWord = strs[0];
//   for (let word of strs) {
//     if (word.length === 0) {
//       return "";
//     }
//     if (shortestWord.length === 0) {
//       shortestWord = word;
//     }
//     if (shortestWord.length > word.length) {
//       shortestWord = word;
//     }
//   }

//   for (let word of strs) {
//     let tempWord = [];
//     for (let index in word) {
//       if (word[index] != firstWord[index]) {
//         break;
//       }
//       if (letters[index] === word[index]) {
//         continue;
//       }
//       tempWord.push(word[index]);
//     }
//     if (tempWord.join("") !== firstWord) {
//       letters.push(tempWord);
//     }
//   }

//   for (let word of letters) {
//     if (word.length === 0) {
//       return shortestWord = "";
//     }
//     if (shortestWord.length === 0) {
//       shortestWord = word.join("");
//     }
//     if (shortestWord.length > word.length) {
//       shortestWord = word.join("");
//     }
//   }

//   return shortestWord;
// };
var longestCommonPrefix = function (strs) {
  result = "";

  for (let index in strs[0]) {
    for (let str of strs) {
      if (index === str.length || str[index] != strs[0][index]) {
        return result;
      }
    }
    result = strs[0][index];
  }
  return result;
};

console.log(longestCommonPrefix(["flower", "flow", "flight"]));
// console.log(longestCommonPrefix(["aa", "aa"]));
// console.log(longestCommonPrefix(["caat", "caa"]));
// console.log(longestCommonPrefix(["", "b"]));
// console.log(longestCommonPrefix(["reflower", "flow", "flight"]));
// console.log(longestCommonPrefix(["c", "acc", "ccc"]));
// console.log(longestCommonPrefix(["aba", "c", "b", "a", "ab"]));

// var longestCommonPrefix = function(strs) {
//     if (strs.length === 0) {
//         return '';
//     }
//     let ans = strs[0];
//     for (let i = 1; i < strs.length; i++) {
//         while (strs[i].indexOf(ans) !== 0) {
//             ans = ans.substring(0, ans.length - 1);
//             if (ans === '') {
//                 return '';
//             }
//         }
//     }
//     return ans;
// };

// var longestCommonPrefix = function(arr) {
//     let i = 1;
//     let prf = arr[0];
//     while(i < arr.length){
//         if(!arr[i].startsWith(prf)){
//             prf = prf.slice(0, -1)
//         }else{
//             i++
//         }
//     }
//     return prf

// };

// var longestCommonPrefix = function(strs) {
//     if(!strs.length) return ""
//     let longestCommonPrefix =""
//     for(let i = 0; i <= strs[0].length - 1; i++){

//         if(strs[0] === "") return ""

//         if(strs.every(str => str[i] === strs[0][i])){
//            longestCommonPrefix +=  strs[0][i]
//         }else{
//             break
//         }
//     }
//     return longestCommonPrefix;
// };

// var longestCommonPrefix = function (strs) {
//     // Return early on empty input
//     if (!strs.length) return '';

//     // Loop through the letters of the first word
//     for (let i = 0; i <= strs[0].length; i++) {
//         // Check if this character is present in the same position of every string
//         if (!strs.every((string) => string[i] === strs[0][i])) {
//             // If not, return the string up to and including the previous character
//             return strs[0].slice(0, i);
//         }
//     }

//     return strs[0];
// };
