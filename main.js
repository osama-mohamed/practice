
/*
    setDate(day[Req]) = day of the month from 1 to 31
    setFullYear(year[Req], month[Opt](0-11 index), day[Opt])
    setHours(hour[Req], minutes[Opt], seconds[Opt], milliseconds[Opt])
    setMinutes(minutes[Req], seconds[Opt], milliseconds[Opt])
    setSeconds(seconds[Req], milliseconds[Opt])
    setMilliseconds(milliseconds[Req])
    setMonth(month[Req](0-11 index), day[opt])
*/


var currentDate  = new Date();
// currentDate.setDate(1);
// currentDate.setFullYear(2016, 9, 1);
// currentDate.setHours(16, 45,45);
// currentDate.setMinutes(44, 46);
// currentDate.setSeconds(42);
// currentDate.setMilliseconds(600000); // 10 minutes
// currentDate.setMonth(3);

console.log(currentDate);
