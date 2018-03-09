
var myString = 'This is a string';

console.log(myString);
console.log(myString.length);
console.log(typeof (myString));


var myNumber = 66;

console.log(myNumber);
console.log(typeof (myNumber));

var myStringNumber = myNumber.toString();   // recommended

console.log(myStringNumber);
console.log(myStringNumber.length);
console.log(typeof (myStringNumber));


var myStringNumberTwo = String(myNumber);   // not recommended

console.log(myStringNumberTwo);
console.log(myStringNumberTwo.length);
console.log(typeof (myStringNumberTwo));