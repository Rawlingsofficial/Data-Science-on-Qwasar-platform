function longest_arithmetic_subsequence_of_given_difference(arr, difference) {
    const dp = new Map();
    let maxLength = 0;
  
    for (let num of arr) {
      dp.set(num, (dp.get(num - difference) || 0) + 1);
      maxLength = Math.max(maxLength, dp.get(num));
    }
  
    return maxLength;
  }
  