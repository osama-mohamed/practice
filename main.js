/*
	removeChild(index)  > remove child element from parent element (elements, text)
*/


var myDiv = document.getElementById('test');


myDiv.removeChild(myDiv.firstElementChild);
myDiv.removeChild(myDiv.childNodes[1]);
myDiv.removeChild(myDiv.children[0]);
