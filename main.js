/*
	contains(element)  > search for element (true, false)
*/


var myDiv = document.getElementById('main'),
	mySpan = document.getElementById('test-span');

if (myDiv.contains(mySpan)) {
	mySpan.textContent = 'Span changed from JavaScript';
}