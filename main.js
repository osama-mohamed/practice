/*
	createAttribute('attribute type : class, id, placeholder')
	setAttributeNode(attribute name)
*/

var myDiv = document.getElementById('test'),
	myAttr = document.createAttribute('class');


myAttr.value = 'osama';

myDiv.setAttributeNode(myAttr);
