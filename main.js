
// window.alert('Hello \nOSAMA MOHAMED \nPython Developer');
alert('Hello \nOSAMA MOHAMED \nPython Developer \nFull stack developer');


// var ask = window.confirm('Are you sure you want to open Google ?');
var ask = confirm('Are you sure you want to open \nGoogle ?');
if (ask === true) {
    window.location.href = 'https://www.google.com.eg';
} else {
    console.log('sorry you choosed not to open Google');
    // window.console.log('sorry you choosed not to open Google');
}


// var name = window.prompt('enter Your name', 'Example: Osama');  // return strings
var name = prompt('enter Your name', 'Example: Osama');      // return strings
console.log(name);