'use strict';

var divs = document.querySelectorAll('div');
var button = document.querySelector('button');

function logText(e) {
  console.log(this.classList.value);
  // e.stopPropagation(); // stop bubbling!
}

divs.forEach(function (div) {
  return div.addEventListener('click', logText, {
    // capture: true, // from root to top
    capture: false, // from top to root
    once: true // run only one time, don not repeat
  });
});

button.addEventListener('click', function () {
  console.log('you click the button');
}, {
  once: true
});