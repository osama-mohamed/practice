/*
	cloneNode()        > copy node and node attributes only
	cloneNode(false)   > copy node and node attributes only
	cloneNode(true)    > copy node and node attributes and text content and his child nodes
*/


var myDiv = document.getElementById('test'),
	myNewDiv = document.getElementById('new'),
	myCopy = myDiv.firstElementChild.cloneNode(true);

myNewDiv.append(myCopy);
console.log(myCopy);
