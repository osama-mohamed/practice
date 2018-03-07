
var friends = [
    'Eslam',
    'Osama',
    'Mohamed',
    'Mahmoud',
    'Ahmed'
];

console.log(friends);

var specialFriends = friends.indexOf('Ahmed', 4);    // search by string and return the index
                                                     // ('item', start search point)
console.log(specialFriends);
console.log(friends[specialFriends]);



var specialFriend = friends.lastIndexOf('Osama', 1);    // search by string and return the index
                                                        // ('item', start search point)
console.log(specialFriend);
console.log(friends[specialFriend]);


document.getElementById('all').innerHTML = 'My Friends : ' + friends;
document.getElementById('special').innerHTML = 'My special Friends : ' + friends[specialFriends];