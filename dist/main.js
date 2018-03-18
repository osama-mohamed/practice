'use strict';

var age = 20;
var age2 = age;
console.log(age, age2);
age = 25;
console.log(age, age2);

var name = 'Os';
var name2 = name;
console.log(name, name2);
name = 'Osama';
console.log(name, name2);

var players = ['Osama', 'Eslam', 'Ahmed', 'Sara'];
var team = players;
console.log(players, team);

var team2 = players.slice();
var team3 = [].concat(players);
var team4 = [].concat(players);
team4[2] = 'Salma';
console.log(team4);

var team5 = Array.from(players);

var person = {
  name: 'Osama Mohamed',
  age: 22
};
var cap2 = Object.assign({}, person, { number: 99, age: 12 });
console.log(cap2);
const cap3 = {...person};
console.log(cap3);


var osama = {
  name: 'Osama',
  age: 20,
  social: {
    github: 'OSAMAMOHAMED1234',
    facebook: 'osama.mohamed.ms'
  }
};
console.log(osama);
var dev = Object.assign({}, osama);
console.log(dev.social.github);
var dev2 = JSON.parse(JSON.stringify(osama));
console.log(dev2.social.github);