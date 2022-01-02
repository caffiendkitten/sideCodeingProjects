// A JavaScript function that will take two string and transpose them

// You will be given an array that contains two strings. Your job is to create a function that will take those two strings and transpose them, so that the strings go from top to bottom instead of left to right.

// Example:
// transposeTwoStrings(['Hello','World']);

// should return:
// H W
// e o
// l r
// l l
// o d





function transposeTwoStrings(strings) {

    var length = Math.max(strings[0].length, strings[1].length);
    var returnArr = [];
    strings[0] = strings[0].split('');
    strings[1] = strings[1].split('');
  
    if (strings[0].length < strings[1].length) {
      for (var i = 0; i < length; i++) {
        if (!strings[0][i]) {
          strings[0][i] = ' ';
        }
      }
    } else if (strings[1].length < strings[0].length) {
      for (var i = 0; i < length; i++) {
        if (!strings[1][i]) {
          strings[1][i] = ' ';
        }
      }
    }
  
    for (var i = 0; i < length; i++) {
      returnArr.push(strings[0][i] + ' ' + strings[1][i]);
    }
  
    return returnArr.join('\n');
  }
  
  console.log("First one:\n",transposeTwoStrings(['Hello','World']));
  console.log("Second one:\n",transposeTwoStrings(['Another','One']));
  console.log("Third one:\n",transposeTwoStrings(['longerString','shortString']));