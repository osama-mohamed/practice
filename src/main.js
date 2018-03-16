/*
	startsWith('string')  > in the first
	endsWith('string')    > in the last
	includes('string')    > from the first to the end


	isFinite()            > check for finite numbers only
	isNaN()               > check for NaN
	isInteger()           > check if number is an integer
*/

let text = `This is a text created by JavaScript`;

console.log(text.startsWith('This'));
console.log(text.endsWith('JavaScript'));
console.log(text.includes('created'));


console.log(Number.isFinite(-6));
console.log(Number.isFinite(6));
console.log(Number.isFinite(6.66));
console.log(Number.isFinite(Infinity));
console.log(Number.isFinite(NaN));


console.log(Number.isNaN(NaN));


console.log(Number.isInteger(6));
console.log(Number.isInteger(-6));
console.log(Number.isInteger(6.66));
console.log(Number.isInteger(Infinity));
console.log(Number.isInteger(NaN));