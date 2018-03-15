/*
	onfocus
	onblur
	onsubmit
*/

var myForm = document.getElementById('test'),
	myNote = document.getElementById('note'),
	myInput = document.forms[0].i1;

myInput.onfocus = function () {
	myNote.textContent = 'write your name';
};

myInput.onblur = function () {
	myNote.textContent = '';
	if (myInput.value.length < 10) {
		myNote.textContent = 'sorry your name must be at least  10 letters';
	}
};

myForm.onsubmit = function (e) {
	e.preventDefault();
};

