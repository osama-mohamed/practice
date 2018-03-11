
var myTextarea = document.getElementById('myarea'),
    mySpan = document.getElementById('myspan');


myTextarea.onkeyup = function () {
    mySpan.textContent = 70 - this.value.length;

    // if condition in short code
    mySpan.textContent < 0 ? mySpan.style.color = '#f00' : mySpan.style.color = '#0f0';

    // // if condition in long code
    // if (mySpan.textContent < 0) {
    //         mySpan.style.color = '#f00';
    // } else if (mySpan.textContent >= 0) {
    //         mySpan.style.color = '#0f0';
    // }
};