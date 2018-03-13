/*
	document.getElementById('div-1')        > ('element id')
	document.getElementsByTagName('div')    > ('element tag name')
	document.getElementsByClassName('test') > ('class name')
	document.querySelectorAll('div.test')   > ('element tag name + .class name OR #id')
*/

document.getElementById('div-1').innerHTML = 'OSAMA MOHAMED';
console.log(document.getElementsByTagName('div'));
console.log(document.getElementsByClassName('test'));
console.log(document.querySelectorAll('div.test'));
