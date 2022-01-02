// This JavaScript code will flip every chunk of 'nth' characters in a string, where n is any positive integer greater than 1. It will then test the expected outcome with the actual outcome to confirm it did as expected.

// Example:
// var input = 'a short example';
// var output = flipEveryNChars(input, 5); --> 'ohs axe trelpma'


function flipEveryNChars(string, n) {
    var splitString = string.split('');
    var flipped = '';
    
    while (splitString.length > 0) {
      flipped += splitString.splice(0, n).reverse().join('');
    }
    return flipped;
  }
  
  function testFlip(actual, expected) {
    if (actual === expected) {
      console.log('passed');
    } else {
      console.log('FAILED');
    }
  }
  
  var string = 'a short example'; 
  var actual = flipEveryNChars(string, 5);
  var expected = 'ohs axe trelpma';
  
  testFlip(actual, expected);