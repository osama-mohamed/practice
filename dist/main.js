'use strict';

var arrow = document.querySelector('.arrow');
var speed = document.querySelector('.speed-value');

navigator.geolocation.watchPosition(function (data) {
  console.log(data);
  speed.textContent = data.coords.speed;
  arrow.style.transform = 'rotate(' + data.coords.heading + 'deg)';
}, function (err) {
  console.error(err);
});