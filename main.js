
var myPassword = document.getElementById('my-password'),
    myButton = document.getElementById('show-password');

/*
myButton.onclick = function () {
    if (this.textContent === 'Show Password') {
    // if (myPassword.getAttribute('type') === 'password') {
        myPassword.setAttribute('type', 'text');
        this.textContent = 'Hide Password';
    } else {
        myPassword.setAttribute('type', 'password');
        this.textContent = 'Show Password';
    }
};
*/


function showHidePassword(element, button) {
    button.onclick = function () {
        // if (this.textContent === 'Show Password') {
        if (element.getAttribute('type') === 'password') {
            element.setAttribute('type', 'text');
            this.textContent = 'Hide Password';
        } else {
            element.setAttribute('type', 'password');
            this.textContent = 'Show Password';
        }
    };
}

showHidePassword(myPassword, myButton);