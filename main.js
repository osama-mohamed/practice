/*
    charAt(index)    | charAt(varName.length - 1) last Char in variable
    charCodeAt(index)
    replace('value', 'new value')
*/

var myString = 'This is a string',
    myChar = myString.charAt(8),
    myCharCode = myString.charCodeAt(8),
    myReplaced = myString.replace('a', 'a new');

console.log(myString);
console.log(myChar);
console.log(myCharCode);
console.log(myReplaced);
