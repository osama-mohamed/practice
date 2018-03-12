/*
    setTimeout(function, milliseconds, param1, para2, param3, ......)
    clearTimeout(id or number of setTimeout function)
*/


setTimeout(function () {
    console.log('Hello osama mohamed after 3 seconds!')
}, 3000);


function writeHello() {
    console.log('Hello osama mohamed after 5 seconds!')
}

var myButton = document.getElementById('click'),
    myMessage = setTimeout(writeHello, 5000);

console.log(myMessage);

myButton.onclick = function () {
    clearTimeout(myMessage);
    clearTimeout(2);
    console.log(myMessage);
};