/*
	childElementCount > get number of children of element (elements only)
	children.length   > get number of children of element (elements only)
	childNodes.length > get number of children of element (elements, text, comments, newlines)
*/


var myDiv = document.querySelector('div');

console.log(myDiv.childElementCount);
console.log(myDiv.children.length);


console.log(myDiv.children);
console.log(myDiv.children[0]);
console.log(myDiv.children[0].textContent);


console.log(myDiv.childNodes);
console.log(myDiv.childNodes.length);
