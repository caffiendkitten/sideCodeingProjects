//  JavaScript funciton to find a pair of numbers in an array and add up to a specific number

// Given a list of non-negative integers and a target sum, find a pair of numbers that sums to the target sum.

// input = array of positive integers and a sum
// output = array of 2 nums that add to that sum
// find two numbers in that input array that add up to that target sum

// Example:
// Input: var pair = findPairForSum([3, 34, 4, 12, 5, 2], 9);
// Output: console.log(pair); // --> [4, 5]




function findPairForSum(array, sum) {
        
    var arrayPair = [];
    var firstInt;
    var secondInt;  
    
    for (i = 0; i < array.length; i++) {
      firstInt = array[i];
      for (k = 0; k < array.length; k++) {
        secondInt = array[k];
        if (firstInt !== secondInt && sum === firstInt + secondInt) {
          arrayPair.push(firstInt, secondInt);
          return arrayPair;
        }
      }
    }
  }
  
  var pair = findPairForSum([3, 34, 4, 12, 5, 2], 9);
  console.log(pair); // --> Expected outcome: [4, 5]