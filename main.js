/*
	document.body
	document.anchors  > a tag with name
	document.links    > a tag with href
*/


document.getElementById('test').innerText = document.body.innerText;
document.getElementById('test-2').innerText = document.anchors.length;

if (document.body.innerText.indexOf('Di') > -1) {
	console.log('i found it!');
}
