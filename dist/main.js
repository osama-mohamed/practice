'use strict';

var _slicedToArray = function () { function sliceIterator(arr, i) { var _arr = []; var _n = true; var _d = false; var _e = undefined; try { for (var _i = arr[Symbol.iterator](), _s; !(_n = (_s = _i.next()).done); _n = true) { _arr.push(_s.value); if (i && _arr.length === i) break; } } catch (err) { _d = true; _e = err; } finally { try { if (!_n && _i["return"]) _i["return"](); } finally { if (_d) throw _e; } } return _arr; } return function (arr, i) { if (Array.isArray(arr)) { return arr; } else if (Symbol.iterator in Object(arr)) { return sliceIterator(arr, i); } else { throw new TypeError("Invalid attempt to destructure non-iterable instance"); } }; }();

var timeNodes = Array.from(document.querySelectorAll('[data-time]'));

var seconds = timeNodes.map(function (node) {
	return node.dataset.time;
}).map(function (timeCode) {
	var _timeCode$split$map = timeCode.split(':').map(parseFloat),
	    _timeCode$split$map2 = _slicedToArray(_timeCode$split$map, 2),
	    mins = _timeCode$split$map2[0],
	    secs = _timeCode$split$map2[1];

	return mins * 60 + secs;
}).reduce(function (total, vidSeconds) {
	return total + vidSeconds;
});

var secondsLeft = seconds;
var hours = Math.floor(secondsLeft / 3600);
secondsLeft = secondsLeft % 3600;

var mins = Math.floor(secondsLeft / 60);
secondsLeft = secondsLeft % 60;

console.log(hours, mins, secondsLeft);

var items = document.querySelectorAll('ul.videos > li');

for (var i = 0; i < items.length; i += 1) {
	items[i].innerText += ' => ' + items[i].dataset.time;
}

items.forEach(function (i) {
	i.innerText += ' => ' + i.dataset.time;
});

items.forEach(function (i) {
	return i.innerText += ' => ' + i.dataset.time;
});
items.forEach(function (i) {
	return i.textContent += ' => ' + i.dataset.time;
});