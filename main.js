/*
    setInterval(function, milliseconds, param1, para2, param3, ......)
    clearInterval(id or number of setInterval function)
*/


setInterval(function () {
    console.log('Hello osama mohamed every 3 seconds!')
}, 3000);


function writeHello() {
    console.log('Hello osama mohamed every 5 seconds!')
}

var myButton = document.getElementById('click'),
    myMessage = setInterval(writeHello, 5000),
    myDiv = document.getElementById('count'),
    myCountDown = setInterval(countDown, 1000);

console.log(myMessage);

myButton.onclick = function () {
    clearInterval(myMessage);
    // clearInterval(2);
    console.log(myMessage);
};




function countDown() {
    if (myDiv.textContent <= 1) {
        myDiv.textContent = 'Done';
        clearInterval(myCountDown);
    } else {
        myDiv.textContent -= 1;
        if (myDiv.textContent < 10) {
            myDiv.textContent = '0' + myDiv.textContent;
        }
    }
}