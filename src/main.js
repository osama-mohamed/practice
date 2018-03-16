/*
function Prefixer(prefix) {
	this.prefix = prefix;
}

Prefixer.prototype.prefixArray = function (arr) {
	let that = this;
	return arr.map(function (x) {
		console.log(that.prefix + x);
	});
};

let pre = new Prefixer('Hello ');
pre.prefixArray(['OSAMA', 'ESLAM']);
*/

function Prefixer(prefix) {
	this.prefix = prefix;
}

Prefixer.prototype.prefixArray = function (arr) {
	return arr.map((x) => {
		console.log(this.prefix + x);
	});
};

let pre = new Prefixer('Hello ');
pre.prefixArray(['OSAMA', 'ESLAM']);


/*
let add = function (a, b) {
	let sum = a + b;
	console.log(sum);
	return false;
};
add(4, 6);
*/



let add = (a, b) => {
	let sum = a + b;
	console.log(sum);
	return false;
};
add(4, 6);