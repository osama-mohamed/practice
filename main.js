/*
	tagName     > get name of element tags only
	nodeName    > get name of tags, text, comment
	nodeValue   > get value of tags, text, comment
	nodeType    > get type of tags, text, comment
	nodeType :
		1 = tag
		2 = attribute
		3 = text
		8 = comment
*/


var myDiv = document.getElementById('test');

console.log(myDiv.childNodes[0].nodeName);
console.log(myDiv.childNodes[1].tagName);

console.log(myDiv.childNodes[0].nodeValue);
console.log(myDiv.childNodes[1].childNodes[0].nodeValue);

console.log(myDiv.childNodes[0].nodeType);