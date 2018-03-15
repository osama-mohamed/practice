/*

*/

var myDiv = document.getElementById('test'),
	myButton = document.querySelector('button');


function changeColor() {
	myDiv.style.color = 'blue';
}

myButton.onclick = changeColor;
