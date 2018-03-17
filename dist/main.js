'use strict';

var pressed = [];
var secretCode = 'osama';

window.addEventListener('keyup', function (e) {
  pressed.push(e.key);
  pressed.splice(-secretCode.length - 1, pressed.length - secretCode.length);
  if (pressed.join('').includes(secretCode)) {
    cornify_add();
  }
});