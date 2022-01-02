// A JavaScript function that will take a string of even and odd numbers, and then find which is the sole even number or the sole odd number. It will then test its accuracy with the an expected outcome against its actual outcome.
// Note:The return value should be 1-indexed, not 0-indexed.

// Examples :
// detectOutlierValue("2 4 7 8 10"); // => 3 - Third number is odd, while the rest of the numbers are even
// detectOutlierValue("1 10 1 1"); //=> 2 - Second number is even, while the rest of the numbers are odd




function detectOutlierValue(string){
    var array = string.split(' ');
    var outlierIndex;
    var evenCount = 0;
    var oddCount = 0;
  
    for (i = 0; i < array.length; i++) {
      if (Math.abs(Math.round(array[i])) % 2 === 0) {
        evenCount++;
        if (evenCount === 1) {
          outlierIndex = i + 1;
        }
      } else {
        oddCount++;
        if (oddCount === 1) {
          outlierIndex = i + 1;
        }
      }
    }
    return outlierIndex;
  }
  
  
  function outlierCheck(expected, actual) {
    if (expected === actual) {
      console.log('PASSED');
    } else {
      console.log('FAILED "' + expected + '" does not equal "' + actual + '"');
    }
  }
  
  
  outlierCheck(detectOutlierValue('-1.2 1.9 11.555 -5'), 2);