'use strict';

var countdown = void 0;
var timerDisplay = document.querySelector('.display__time-left');
var endTime = document.querySelector('.display__end-time');
var buttons = document.querySelectorAll('[data-time]');

function timer(seconds) {
  clearInterval(countdown);
  var now = Date.now();
  var then = now + seconds * 1000;
  displayTimeLeft(seconds);
  displayEndTime(then);
  countdown = setInterval(function () {
    var secondsLeft = Math.round((then - Date.now()) / 1000);
    if (secondsLeft < 0) {
      clearInterval(countdown);
      return;
    }
    displayTimeLeft(secondsLeft);
  }, 1000);
}

function displayTimeLeft(seconds) {
  var minutes = Math.floor(seconds / 60);
  var remainderSeconds = seconds % 60;
  var display = '' + (minutes < 10 ? '0' : '') + minutes + ':' + (remainderSeconds < 10 ? '0' : '') + remainderSeconds;
  document.title = display;
  timerDisplay.textContent = display;
}

function displayEndTime(timestamp) {
  var end = new Date(timestamp);
  var hour = end.getHours();
  var adjustedHour = hour > 12 ? hour - 12 : hour;
  var minutes = end.getMinutes();
  endTime.textContent = 'Be Back At ' + adjustedHour + ':' + (minutes < 10 ? '0' : '') + minutes;
}

function startTimer() {
  var seconds = parseInt(this.dataset.time);
  timer(seconds);
}

buttons.forEach(function (button) {
  return button.addEventListener('click', startTimer);
});
document.customForm.addEventListener('submit', function (e) {
  e.preventDefault();
  var mins = this.minutes.value;
  timer(mins * 60);
  this.reset();
});