/*
	classList;                  > get array of element classes
	classList.value;            > get classes as a string
	classList.contains('osama') > check if class is exists ('class name)
	classList.item(3)           > get class name of index as a string
*/


var myDiv = document.querySelector('div');

console.log(myDiv.classList);
console.log(myDiv.classList.value);
console.log(myDiv.classList.length);
console.log(myDiv.classList.item(3));

if (myDiv.classList.contains('osama')) {
	console.log('Hello osama');
}
