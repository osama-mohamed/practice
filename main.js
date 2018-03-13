/*
	document.title
	document.images
	document.forms
*/

document.getElementById('test').innerHTML = document.title;
document.getElementById('test-2').innerHTML = document.images[0].src;
document.getElementById('test-3').innerText = document.forms[0].i2.value; // type


for (var i = 0; i < document.images.length; i += 1) {
	document.write('<br>' + document.images[i].src);
}