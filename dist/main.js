'use strict';

function removeTransition(e) {
	if (e.propertyName !== 'transform') return;
	e.target.classList.remove('playing');
}

function playSound(e) {
	var audio = document.querySelector('audio[data-key="' + e.keyCode + '"]');
	var key = document.querySelector('div[data-key="' + e.keyCode + '"]');
	if (!audio) return;

	key.classList.add('playing');
	audio.currentTime = 0;
	audio.play();
}

var keys = Array.from(document.querySelectorAll('.key'));
keys.forEach(function (key) {
	return key.addEventListener('transitionend', removeTransition);
});
window.addEventListener('keydown', playSound);