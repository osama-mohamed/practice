
function myAgeInHours(myAge) {
    return myAge * 365 * 24;
}

var askForAge = prompt('what is your age ? ');

document.getElementById('test').innerHTML = 'My Age in Hours = ' + myAgeInHours(askForAge) + ' Hours';