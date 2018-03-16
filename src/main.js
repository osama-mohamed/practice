
let myArray = [2, 4, 6, 8, 10],
	mySet = new Set(myArray);

mySet.add('12');
mySet.add(20);
mySet.add({a: 1, b: 'OSAMA'});
mySet.delete(8);
mySet.clear();

console.log(mySet);
console.log(mySet.size);

mySet.forEach(function (val) {
	console.log(val);
});


// -----------------------------------------------


let myMap = new Map([['a', 'ahmed'], ['b', 'basma']]);

myMap.set('s', 'salma');
myMap.delete('a');

console.log(myMap);
console.log(myMap.size);


// -----------------------------------------------


let carWeakSet = new WeakSet();

let car1 = {
	name: 'honda',
	model: 'civic'
};

let car2 = {
	name: 'bmw',
	model: 'f5'
};

carWeakSet.add(car1);
carWeakSet.add(car2);
carWeakSet.delete(car1);

console.log(carWeakSet);

// -----------------------------------------------

let carWeakMap = new WeakMap();

let key1 = {
	id: 1
};

let c1 = {
	name: 'honda',
	model: 'civic'
};

let key2 = {
	id: 2
};

let c2 = {
	name: 'bmw',
	model: 'f5'
};

carWeakMap.set(key1, c1);
carWeakMap.set(key2, c2);

carWeakMap.delete(key1);

console.log(carWeakMap);