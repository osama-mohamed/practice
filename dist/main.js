'use strict';

var checkboxes = document.querySelectorAll('.inbox input[type="checkbox"]');

var lastChecked = void 0;

function handleCheck(e) {
  var _this = this;

  var inBetween = false;
  if (e.shiftKey && this.checked) {
    checkboxes.forEach(function (checkbox) {
      if (checkbox === _this || checkbox === lastChecked) {
        inBetween = !inBetween;
      }
      if (inBetween) {
        checkbox.checked = true;
      }
    });
  }
  lastChecked = this;
}

checkboxes.forEach(function (checkbox) {
  return checkbox.addEventListener('click', handleCheck);
});