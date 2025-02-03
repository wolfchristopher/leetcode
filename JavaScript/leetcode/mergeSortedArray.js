var merge = function (nums1, m, nums2, n) {
//   nums2 = nums2.slice(0, n).sort();
//   console.log(nums2)
  return nums1.slice(0, m)
//   .push(...nums2.slice(0, n).sort());

//   return nums1.sort();
};

console.log(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3));
console.log(merge([1], 1, [], 0));
console.log(merge([0], 0, [1], 1));
