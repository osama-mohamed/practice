/*
	getAttribute('attribute');                     > get
	setAttribute('attribute', 'new value') = '';   > set
*/


var myDiv = document.querySelector('div');

console.log(myDiv.getAttribute('id'));
console.log(myDiv.getAttribute('class'));

myDiv.setAttribute('id', 'OSAMA');
myDiv.setAttribute('class', 'OSAMA');

