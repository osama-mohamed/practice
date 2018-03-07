
var friends = [ // literal way
    'Eslam',
    'Mohamed',
    'Mahmoud'
];

console.log(friends);

if (Array.isArray(friends)) {         // first check if this is an array
    console.log('yes it is array');
} else {
    console.log('no it is not array');
}


if (friends.constructor === Array) {  // second check if this is an array
    console.log('yes it is array');
} else {
    console.log('no it is not array');
}