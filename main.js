
var myInput = document.getElementById('test-input'),
    myDiv = document.getElementById('test');

myInput.onkeyup = function () {
    myDiv.innerHTML = myInput.value * 20;
};