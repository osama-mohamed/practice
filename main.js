/*
	parentNode      > get the parent of node, element
	parentElement   > get the parent of element only   (recommended to use)
*/


var myDiv = document.getElementById('test'),
	myButton = myDiv.lastElementChild;


console.log(myButton.parentNode);
console.log(myButton.parentElement);

console.log(myDiv.parentElement.tagName);

myButton.onclick = function () {
	this.parentElement.style.display = 'None';
};


if (myDiv.parentElement.tagName === 'BODY') {
	console.log('Yes, this parent is body!');
}