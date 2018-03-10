
/*
    regular expression syntax
    /pattern/attributes

    Attributes List :
    i   => case insensitive
    g   => global
    m   => multi line search

    [char]      => character
    [^char]     => not character
    [a-zA-Z]    => range small and capital letters
    [^a-zA-Z]   => not range small and capital letters
    [0-9]       => range from 0 to 9
    [^0-9]      => not range from 0 to 9
    [A-g]       => range [A-Z] and range [a-g]
    [0-9a-z]    => range [0-9] and range [a-z]
*/


var myString = 'This 1 is 2 a 6 string 9',
    result = myString.replace(/[^a-z0-9 ]/g, '@');

console.log(result);
