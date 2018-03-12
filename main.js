/*
	scrollBy(x, y)	> (100, 400) (x)positive number to right or down, (y)negative number to left or up
	// increased scroll


	scrollTo(x, y)	> (100, 400) (x)positive number to right or down, (y)negative number to left or up
	// scroll to position and stop permanently
*/

document.getElementById('scroll-by').onclick = function () {
	window.scrollBy(200, 150);				// window.scrollBy(-200, -150);
	window.console.log('window scrolled from left ' + window.scrollX + ' px.');
	window.console.log('window scrolled from top ' + window.scrollY + ' px.');
};

document.getElementById('scroll-to').onclick = function () {
	window.scrollTo(200, 150);
	window.console.log('window scrolled from left ' + window.scrollX + ' px.');
	window.console.log('window scrolled from top ' + window.scrollY + ' px.');
};