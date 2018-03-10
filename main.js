
/*
    full format = new Date("october 01 1994 01:01:01")
    long format = new Date("october 01 1994 01:01:01")
    short format = new Date("10/1/1994 01:01:01")
    iso format = new Date("1994-10-01 01:01:01+02:00")
*/


var full  = new Date('october 01 1994 01:01:01'),
    long = new Date('october 01 1994 01:01:01'),
    short = new Date('10/1/1994 01:01:01'),
    iso = new Date('1994-10-01 01:01:01+02:00');

console.log(full);
console.log(long);
console.log(short);
console.log(iso);