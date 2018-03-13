/*
	classList.add('js', 'css', 'html')    > add class on element ('class name', 'other class name')
	classList.remove('js', 'css', 'html') > remove class on element ('class name', 'other class name')
	classList.toggle('microsoft')         > toggle class on element ('class name')
*/


var myDiv = document.querySelector('div'),
	myButton = document.querySelector('button'),
	myRemoveButton = document.getElementById('remove'),
	myToggleButton = document.getElementById('toggle');

myButton.onclick = function () {
	// myDiv.className += ' js';
	myDiv.classList.add('js', 'css', 'html');
};

myRemoveButton.onclick = function () {
	myDiv.classList.remove('js', 'css', 'html');
};

myToggleButton.onclick = function () {
	myDiv.classList.toggle('microsoft');
};
