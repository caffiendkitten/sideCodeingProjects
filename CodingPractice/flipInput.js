// Javascript function to reverse the input

function flipPairs(string){
    var split = string.split('');
    var flippedString = '';
    
    while(split.length >0){
      flippedString += split.splice(0,2).reverse().join('');
    }
    return flippedString;
    
}
function testFlips(actual, expected) {
    if (actual === expected) {
        console.log('passed');
    } else {
        console.log('FAILED');
    }
}

var actual = flipPairs('check out how interesting this problem is, it\'s insanely interesting!');
var expected = 'hcce kuo toh wnietertsni ghtsip orlbmei ,si \'t sniasenyli tnreseitgn!';

console.log(actual);

console.log(testFlips(actual, expected));


  
  
  