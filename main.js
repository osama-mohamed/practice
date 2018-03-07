
var friends = [
    'Eslam',
    'Osama',
    'Mohamed',
    'Mahmoud',
    'Ahmed',
    1,
    2,
    10,
    20,
    11,
    21
];

console.log(friends);

var sliced= friends.slice(2, 4);    // (start, stop) from first
console.log(sliced);

var slicedFromEnd= friends.slice(-10, -6);    // (start, stop) from last
console.log(slicedFromEnd);

var newFriends = [
    'Ebram',
    'Mikel',
    'Mina'
];

var workFriends = [
    'Mariem',
    'Basma',
    'norhan'
];

// concatenation newFriends and workFriends to friends
var allFriends = friends.concat(newFriends, workFriends);
console.log(allFriends);