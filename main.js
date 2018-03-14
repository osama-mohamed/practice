/*
	scrollTop    > scroll from top number of pixels
	scrollLeft   > scroll from left number of pixels
*/

var myDiv = document.getElementById('main');


myDiv.onclick = function () {
	document.documentElement.scrollTop += 100;
	console.log(document.documentElement.scrollTop);

	if (document.documentElement.scrollTop >= 1000) {
		this.classList.add('active');
	}
};
