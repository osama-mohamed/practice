/*
	firstElementChild   > get first element child of element (elements only)
	lastElementChild    > get last element child of element (elements only)

	firstChild          > get first child of element  (elements, text, comments, newlines)
	lastChild           > get last child of element (elements, text, comments, newlines)
*/


var myDiv = document.querySelector('div');

console.log(myDiv.firstElementChild);
console.log(myDiv.children[0]);

console.log(myDiv.lastElementChild);
console.log(myDiv.children[1]);


console.log(myDiv.firstChild);
console.log(myDiv.childNodes[0]);

console.log(myDiv.lastChild);
console.log(myDiv.childNodes[5]);

