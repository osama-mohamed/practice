
function *g1() {
	console.log('Hello');
	yield 'Yield 1 Started !';
	console.log('World');
	yield 'Yield 2 Started !';
	return 'Return';
}

var g = g1();

console.log(g.next());  // first yield & done = false
console.log(g.next());  // second yield & done = false
console.log(g.next());  // return & done = true


/*
console.log(g.next().value);
console.log(g.next().value);
console.log(g.next().value);
*/

console.log('**********');

for(let val of g) {
	console.log(val);
}