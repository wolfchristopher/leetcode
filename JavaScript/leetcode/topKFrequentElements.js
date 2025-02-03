var topKFrequent = function (nums, k) {
  let map = new Map();
  for (let num of nums) {
    if (!map.has(num)) {
      map.set(num, 0);
    }
    const currentValue = map.get(num);
    map.set(num, currentValue + 1);
  }
  const mapArray = [...map.entries()]

/*
  What is going on on the line below?
   Comparison function (a, b) => b[1] - a[1]: This is the function used to determine the order of the elements. Here’s how it works:

    - a and b: These are two elements from the mapArray that the sort method compares. Each a and b is an array in the form [key, value].
    - b[1] and a[1]: These refer to the second element of the arrays a and b, respectively, which are the values from the Map.
    - b[1] - a[1]: This expression calculates the difference between the value of b and the value of a.
    
    Descending order: The sort method sorts the array based on the return value of the comparison function:

    - If the return value is negative, a comes before b.
    - If the return value is positive, a comes after b.
    - If the return value is zero, a and b are considered equal.
    
    By using b[1] - a[1], we ensure that elements with larger values come before elements with smaller values, 
    resulting in a descending order sort based on the values. Here’s a step-by-step example to illustrate:
*/
  mapArray.sort((a, b) => b[1] - a[1])
  /*

  */
  const topK = mapArray.slice(0, k)
  /*

  */
  return topK.map(element => element[0]);
};

console.log(topKFrequent([1, 1, 1, 2, 2, 3], 2));
