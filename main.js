
var myInput = document.getElementById('test-input'),
    myDiv = document.getElementById('test'),
    myCurrency = document.getElementById('currency');


// myDiv.onmouseover = function () {
//     myDiv.innerHTML = 'You hovered me';
// };
//
// myDiv.onmouseout = function () {
//     myDiv.innerHTML = 'You moved out of me';
// };
//
// myInput.onkeyup = function () {
//     myDiv.innerHTML = myInput.value * 20;
// };

myCurrency.onchange = function () {
    myDiv.innerHTML = myInput.value * myCurrency.value;
};