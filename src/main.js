var v = `osama`;
console.log(v);


let o = `osama`;
console.log(o);


function testVar() {
	var a = 66;
	if (true) {
		var a = 44;
		console.log(a);
	}
	console.log(a);
}
testVar();

console.log('**********');


function testLet() {
	let a = 66;
	if (true) {
		let a = 44;
		console.log(a);
	}
	console.log(a);
}
testLet();


for (var i = 0; i < 10; i += 1) {
	console.log(i);
}
console.log('end of for loop with var');
console.log(i);

console.log('*******');

for (let l = 0; l < 10; l += 1) {
	console.log(l);
}
console.log('end of for loop with let');
console.log(l);