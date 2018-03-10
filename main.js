
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
    letter+                      => word contain more than number of letter
    letter{number}               => word contain number of letter
    letter{number1, number2}     => word contain number1 of letter or number2 of letter
    letter{number,}              => word contain more than number of letter
*/


var myString = 'This 1 ihhs 2 ahhh 6 sthhhhring 9',
    result = myString.replace(/h{2,}/g, '@');

console.log(result);
