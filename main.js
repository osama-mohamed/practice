/*
    split(separator, limit)
    slice(start, end)
    substr(start, length)
    substring(start, end)
*/

var myString = 'This is a string',
    mySplittedString = myString.split(' ', 2),
    mySlicedString = myString.slice(8, 16),    // slice(-5)  the last 5 char in string
    mySubStr = myString.substr(8, 8),
    mySubString = myString.substring(8, 16);

console.log(myString);
console.log(typeof (myString));

console.log(mySplittedString);
console.log(typeof (mySplittedString));

console.log('************');
console.log(mySlicedString);
console.log(typeof (mySlicedString));

console.log('------');
console.log(mySubStr);
console.log(typeof (mySubStr));

console.log('+++++++++');
console.log(mySubString);
console.log(typeof (mySubString));