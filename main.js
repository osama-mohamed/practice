
/*
    getDate = day of the month from 1 to 31
    getDay = day of the week from 0 to 6 >> sun == 0 & sat == 6
    getFullYear
    getHours
    getMinutes
    getSeconds
    getMilliseconds
    getTime = milliseconds from 1 jan 1970 until now
    getTimezoneOffset = difference between utc and local time in minutes
*/


var currentDate  = new Date(),
    day = currentDate.getDate(),
    dayOfWeek = currentDate.getDay(),
    fullYear = currentDate.getFullYear(),
    hours = currentDate.getHours(),
    minutes = currentDate.getMinutes(),
    seconds = currentDate.getSeconds(),
    milliSeconds = currentDate.getMilliseconds(),
    milliSecondsFrom1970 = currentDate.getTime(),
    timeZoneOffset = currentDate.getTimezoneOffset();

console.log(currentDate);
console.log(day);
console.log(dayOfWeek);
console.log(fullYear);
console.log(hours);
console.log(minutes);
console.log(seconds);
console.log(milliSeconds);
console.log(milliSecondsFrom1970);
console.log(timeZoneOffset);
