
function myAgeInHours() {
    var myAge = 23;
    return myAge * 365 * 24;
}

document.getElementById('test').innerHTML = 'My Age in Hours = ' + myAgeInHours() + ' Hours';