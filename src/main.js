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
