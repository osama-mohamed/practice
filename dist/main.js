'use strict';

var triggers = document.querySelectorAll('.cool > li');
var background = document.querySelector('.dropdownBackground');
var nav = document.querySelector('.top');

function handleEnter() {
  var _this = this;

  this.classList.add('trigger-enter');
  setTimeout(function () {
    return _this.classList.contains('trigger-enter') && _this.classList.add('trigger-enter-active');
  }, 150);
  background.classList.add('open');

  var dropdown = this.querySelector('.dropdown');
  var dropdownCoords = dropdown.getBoundingClientRect();
  var navCoords = nav.getBoundingClientRect();

  var coords = {
    height: dropdownCoords.height,
    width: dropdownCoords.width,
    top: dropdownCoords.top - navCoords.top,
    left: dropdownCoords.left - navCoords.left
  };

  background.style.setProperty('width', coords.width + 'px');
  background.style.setProperty('height', coords.height + 'px');
  background.style.setProperty('transform', 'translate(' + coords.left + 'px, ' + coords.top + 'px)');
}

function handleLeave() {
  this.classList.remove('trigger-enter', 'trigger-enter-active');
  background.classList.remove('open');
}

triggers.forEach(function (trigger) {
  return trigger.addEventListener('mouseenter', handleEnter);
});
triggers.forEach(function (trigger) {
  return trigger.addEventListener('mouseleave', handleLeave);
});