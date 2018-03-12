
var myElement = document.getElementById('type'),
    myButton = document.getElementById('start-button'),
    myText = 'This is a test text from JavaScript!';

/*
myButton.onclick = function () {
    var i = 0,
    typeWriter = setInterval(function () {
        myElement.textContent += myText[i];
        i += 1;
        if (i === myText.length) {
        // if (i >= myText.length) {
        // if (i > myText.length -1) {
            clearInterval(typeWriter);
        }
    }, 200);
};
*/


function typeTextWriter(element, button, text) {
    var i = 0;
    button.onclick = function () {
        var typeWriter = setInterval(function () {
            element.textContent += text[i];
            i += 1;
            if (i === text.length) {
            // if (i >= text.length) {
            // if (i > text.length -1) {
                clearInterval(typeWriter);
            }
        }, 200);
    };
}

typeTextWriter(myElement, myButton, myText);
