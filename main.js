/*
    trim()
    link()
*/

var myString = '           This is a string          ',
    myTrimmedString = myString.trim();

console.log(myString);
console.log(myTrimmedString);



var myOtherString = 'Google',
    myLinkedString = myOtherString.link('https://www.google.com.eg');

console.log(myOtherString);
console.log(myLinkedString);
