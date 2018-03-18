
let age = 20;
let age2 = age;
console.log(age, age2);
age = 25;
console.log(age, age2);

let name = 'Os';
let name2 = name;
console.log(name, name2);
name = 'Osama';
console.log(name, name2);

const players = ['Osama', 'Eslam', 'Ahmed', 'Sara'];
const team = players;
console.log(players, team);


const team2 = players.slice();
const team3 = [].concat(players);
const team4 = [...players];
team4[2] = 'Salma';
console.log(team4);


const team5 = Array.from(players);


const person = {
  name: 'Osama Mohamed',
  age: 22
};
const cap2 = Object.assign({}, person, { number: 99, age: 12 });
console.log(cap2);
const cap3 = {...person};
console.log(cap3);


const osama = {
  name: 'Osama',
  age: 20,
  social: {
	github: 'OSAMAMOHAMED1234',
	facebook: 'osama.mohamed.ms'
  }
};
console.log(osama);
const dev = Object.assign({}, osama);
console.log(dev.social.github);
const dev2 = JSON.parse(JSON.stringify(osama));
console.log(dev2.social.github);
