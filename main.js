
var hasDiscount = false; // boolean

if (hasDiscount === true) {
    var mainPrice = 350;
} else {
    var mainPrice = 500;
}

document.getElementById('price').innerHTML = mainPrice;


var social = ['facebook.com', 'youtube.com', 'google.com']; // array

document.getElementById('social-web').innerHTML = social[0];


var myFullName = {firstName:'osama', lastName: 'mohamed'}; // object

document.getElementById('full-name').innerHTML = myFullName.firstName;

var myName = "osama \"mohamed\" "; // string   \" to escape from closing the string

document.getElementById('name').innerHTML = myName;

var myAge = 23; // number

document.getElementById('age').innerHTML = myAge;
