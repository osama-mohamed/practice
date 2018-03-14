/*
	addEventListener('event', function)     > add event listener on the element
	removeEventListener('event', function)  > remove event listener from the element
*/


var myMainButton = document.getElementById('main'),
	myPowerButton = document.getElementById('power');


myMainButton.onclick = function () {
	document.getElementById('monster-1').style.display = 'none';
};


myPowerButton.onclick = function () {
	myMainButton.addEventListener('click', function () {
		document.getElementById('monster-2').style.display = 'none';
	});
};
