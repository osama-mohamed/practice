
var friends = [
    'Eslam',
    'Mohamed',
    'Mahmoud'
];

console.log(friends);

friends = friends.toString();            // convert array to string
console.log(friends);

friends = friends.toLocaleString();     // convert array to string
console.log(friends);

friends = friends.join();               // convert array to string
console.log(friends);

friends = friends.join('-');            // convert array to string
console.log(friends);


var myDate = new Date(),
    myString = myDate.toString(),
    myLocaleString = myDate.toLocaleString();

console.log(myDate);
console.log(myString);
console.log(myLocaleString);