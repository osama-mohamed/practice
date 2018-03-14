/*
	focus()  > focus on the element
	blur()   > blur from the element
*/


var myForm = document.getElementById('test'),
	myInput = document.getElementById('my-input'),
	myButton = document.querySelector('button');


window.onload = function () {
	myInput.focus();
};

myButton.onclick = function () {
	myInput.blur();
};