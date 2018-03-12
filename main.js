/*
	window.document.cookie > read cookies
	window.document.cookie('name=value; expires=Wed Mar 14 2018 20:10:50 GMT+0200; path=/') set cookie
*/


window.console.log(window.document.cookie);
window.console.log(window.document.cookie = 'name=OSAMA; expires=Mon Mar 12 2018 22:10:50 GMT+0200; path=/'); // create
window.console.log(window.document.cookie = 'name=OSAMA Mohamed; expires=Mon Mar 15 2018 22:10:50 GMT+0200; path=/'); // update
window.console.log(window.document.cookie = 'name=; expires=Mon Mar 12 2018 20:10:50 GMT+0200; path=/'); // delete
window.console.log(window.document.cookie);

