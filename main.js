
var myNumber = 660,
    myString = myNumber.toString(),
    myNewNumber = myString.replace(0, 6),
    mySplitted = myNewNumber.split('');


console.log(myNumber);
console.log(myString);
console.log(myNewNumber);
console.log(mySplitted);


var myNumberTwo = 660,
    chainNumber = myNumberTwo.toString().replace(0, 6).split('');

console.log(chainNumber);
