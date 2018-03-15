/*
	onclick
	ondblclick
	oncontextmenu
	onmouseenter
	onmouseleave
*/

var myDiv = document.getElementById('test'),
	myNote = document.getElementById('note');

myDiv.onclick = function () {
	myNote.textContent = 'you clicked on me';
};

myDiv.ondblclick = function () {
	myNote.textContent = 'you double clicked on me';
};

myDiv.oncontextmenu = function (e) {
	e.preventDefault();
	myNote.textContent = 'you can not right click here';
};

myDiv.onmouseenter = function () {
	myNote.textContent = 'welcome';
};

myDiv.onmouseleave = function () {
	myNote.textContent = 'good bye';
};

