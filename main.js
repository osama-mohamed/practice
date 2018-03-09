/*
    String.fromCharCode(num1, num2, num3, num4, ...........)
    concat(string, string, ....)
*/

var myName = String.fromCharCode(79, 115, 97, 109, 97),
    myNameCap = String.fromCharCode(79, 83, 65, 77, 65),
    myString = 'This is a string',
    myStringTwo = 'This is a second string',
    concatString = myString.concat(' ', myStringTwo),
    concatStringTwo = 'This is a string'.concat(' ', 'This is a second string');

console.log(myName);
console.log(myNameCap);

console.log(concatString);
console.log(concatStringTwo);
