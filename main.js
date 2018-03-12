/*
	stop()	> stop loading the website
	close() > close pages that has been opened by javascript
	focus() > focus on pages opened by javascript
*/

document.getElementById('stop').onclick = function () {
	window.stop();
};


var popupWindow = window.open('https://www.google.com.eg', 'Google', 'height=100, width=100');
document.getElementById('close').onclick = function () {
	popupWindow.close();
};

document.getElementById('focus').onclick = function () {
	popupWindow.focus();
};