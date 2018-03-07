
var friends = [
    'Eslam',
    'Mohamed',
    'Mahmoud'
];

console.log(friends);
console.log(friends.length);


friends[3] = 'Osama';
console.log(friends);
console.log(friends.length);

friends[friends.length] = 'Sara';   // insert Sara at the last
console.log(friends);
console.log(friends.length);

friends.push('Nariman');            // insert Nariman at the last
console.log(friends);
console.log(friends.length);

friends.unshift('Mai');             // insert Mai at the first
console.log(friends);
console.log(friends.length);

friends.splice(5, 1);              // (start on index, number of how many to delete)
console.log(friends);
console.log(friends.length);

friends.splice(5, 0, 'Ahmed', 'Ali', 'Mona'); // (start on index, don't delete, add something)
console.log(friends);
console.log(friends.length);