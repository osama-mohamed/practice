
var friends = [
    'Eslam',
    'Osama',
    'Mohamed',
    'Mahmoud'
];

console.log(friends);
console.log(friends.length);

friends.splice(3, 1);              // (start on index, number of how many to delete)
console.log(friends);
console.log(friends.length);

friends.pop();                    // delete the last index
console.log(friends);
console.log(friends.length);

friends.shift();                  // delete the first index
console.log(friends);
console.log(friends.length);