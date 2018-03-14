/*
	nextElementSibling       > get the next sibling of element only      (recommended to use)
	previousElementSibling   > get the previous sibling of element only  (recommended to use)

	nextSibling       > get the next sibling of node, element
	previousSibling   > get the previous sibling of node, element
*/


var myDiv = document.getElementById('test');


console.log(myDiv.childNodes[1].nextElementSibling);
console.log(myDiv.childNodes[3].previousElementSibling);

console.log(myDiv.childNodes[1].nextSibling);
console.log(myDiv.childNodes[1].previousSibling);


myDiv.childNodes[3].previousElementSibling.textContent += ' changed by js';