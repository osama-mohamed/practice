
/*
    regular expression syntax
    /pattern/attributes

    Attributes List :
    i   => case insensitive
    g   => global
    m   => multi line search
*/


var myString = 'This is a string',
    result = myString.replace(/i/gi, '@');

console.log(result);
