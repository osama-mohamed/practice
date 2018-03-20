'use strict';

var holes = document.querySelectorAll('.hole');
var scoreBoard = document.querySelector('.score');
var moles = document.querySelectorAll('.mole');
var lastHole = void 0;
var timeUp = false;
var score = 0;

function randomTime(min, max) {
  return Math.round(Math.random() * (max - min) + min);
}

function randomHole(holes) {
  var idx = Math.floor(Math.random() * holes.length);
  var hole = holes[idx];
  if (hole === lastHole) {
    return randomHole(holes);
  }
  lastHole = hole;
  return hole;
}

function peep() {
  var time = randomTime(200, 1000);
  var hole = randomHole(holes);
  hole.classList.add('up');
  setTimeout(function () {
    hole.classList.remove('up');
    if (!timeUp) peep();
  }, time);
}

function startGame() {
  scoreBoard.textContent = 0;
  timeUp = false;
  score = 0;
  peep();
  setTimeout(function () {
    return timeUp = true;
  }, 10000);
}

function bonk(e) {
  if (!e.isTrusted) return;
  score++;
  this.parentNode.classList.remove('up');
  scoreBoard.textContent = score;
}

moles.forEach(function (mole) {
  return mole.addEventListener('click', bonk);
});