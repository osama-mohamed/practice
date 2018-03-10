
/*
    new Date()                  => current date and time
    new Date(10000)             => 10000 milliseconds == 10 seconds
    new Date("dateString")      => date as a string
    new Date(year, month, day, hour, minute, second, millisecond)      => date as a string
*/


var currentDate = new Date(),
    milliseconds = new Date(1000),
    dateString  = new Date('october 01 1994 00:00:00'),
    numberedDate = new Date(1994, 9, 1, 0, 0, 0, 0);

console.log(currentDate);
console.log(milliseconds);
console.log(dateString);
console.log(numberedDate);