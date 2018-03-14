/*
	click()  > click on the element
*/


var myDiv = document.getElementById('test'),
	myButton = myDiv.firstElementChild;


myButton.onclick = function () {
	this.parentElement.style.display = 'none';
};


window.onload = function () {
	myButton.click();
};

