
/*
    now()       // to present
    parse()     // to specific date
    toISOString()
    toDateString()
    toTimeString()
*/


var currentDate  = new Date(),
    now = Date.now(),
    parse = Date.parse('1 Oct 1994'),
    min = 1000 * 60,
    hour = min * 60,
    day = hour * 24,
    month = day * 30,
    year = day * 365,
    iso = currentDate.toISOString(),
    date = currentDate.toDateString(),
    time = currentDate.toTimeString();


console.log(currentDate);
console.log(Math.round(now / year));
console.log(Math.round(parse / year));

console.log(iso);
console.log(date);
console.log(time);
