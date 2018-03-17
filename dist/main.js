'use strict';

function _toConsumableArray(arr) { if (Array.isArray(arr)) { for (var i = 0, arr2 = Array(arr.length); i < arr.length; i++) { arr2[i] = arr[i]; } return arr2; } else { return Array.from(arr); } }

var people = [{ name: 'Wes', year: 1988 }, { name: 'Kait', year: 1986 }, { name: 'Irv', year: 1970 }, { name: 'Lux', year: 2015 }];

var comments = [{ text: 'Love this!', id: 523423 }, { text: 'Super good', id: 823423 }, { text: 'You are the best', id: 2039842 }, { text: 'Ramen is my fav food ever', id: 123523 }, { text: 'Nice Nice Nice!', id: 542328 }];

// const isAdult = people.some(function(person) {
//   const currentYear = (new Date()).getFullYear();
//   if(currentYear - person.year >= 19) {
//     return true;
//   }
// });

var isAdult = people.some(function (person) {
  return new Date().getFullYear() - person.year >= 19;
});
console.log({ isAdult: isAdult });

var allAdults = people.every(function (person) {
  return new Date().getFullYear() - person.year >= 19;
});
console.log({ allAdults: allAdults });

var comment = comments.find(function (comment) {
  return comment.id === 823423;
});
console.log(comment);

var index = comments.findIndex(function (comment) {
  return comment.id === 823423;
});
console.log(index);

// comments.splice(index, 1);

var newComments = [].concat(_toConsumableArray(comments.slice(0, index)), _toConsumableArray(comments.slice(index + 1)));