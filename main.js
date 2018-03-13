/*
	hasAttribute('id');             > check (true, false)
	removeAttribute('attribute');   > remove
*/


var myDiv = document.querySelector('div');

console.log(myDiv.hasAttribute('id'));
console.log(myDiv.hasAttribute('data-name'));

myDiv.removeAttribute('class');

if (myDiv.hasAttribute('id')) {
	console.log('yes');
} else {
	console.log('no');
}

