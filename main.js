/*
	createElement('tag type : div, p')
	createTextNode('text here')
	createComment('comment here')
*/

var myMainDiv = document.createElement('div'),
	myText = document.createTextNode('This text created by JavaScript!'),
	myComment = document.createComment('This comment created by JavaScript!');


document.body.appendChild(myMainDiv);


myMainDiv.appendChild(myComment);
myMainDiv.appendChild(myText);

