

var seconds = 122,
    countDiv = document.getElementById('countdown'),
    countDown = setInterval(function () {
        secondPass();
    }, 1000);

function secondPass() {
    var minutes = Math.floor(seconds / 60),
        remSeconds = seconds % 60;
    if (remSeconds < 10) {            // if second less than 10 > put 0 before it
        remSeconds = '0' + remSeconds;
    }
    if (minutes < 10) {               // if minute less than 10 > put 0 before it
        minutes = '0' + minutes;
    }
    countDiv.innerHTML = minutes + ' : ' + remSeconds;   //put the counter inside the div
    if (seconds > 0) {                // if there is time > decrease it
        seconds -= 1;                 // decrease one second every 1000 milliseconds
    } else {
        clearInterval(countDown);     // stop count down timer
        countDiv.innerHTML = 'Done';  // message to appear when timer ended
    }
}