/*
	onkeydown
	onkeypress
	onkeyup
*/

var myInput = document.getElementById('test'),
	myNote = document.getElementById('note');

myInput.onkeyup = function () {
	myNote.textContent = myInput.value;
};
