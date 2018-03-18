'use strict';

var hero = document.querySelector('.hero');
var text = hero.querySelector('h1');
var walk = 500;

function shadow(e) {
	var width = hero.offsetWidth,
	    height = hero.offsetHeight;
	var x = e.offsetX,
	    y = e.offsetY;

	if (this !== e.target) {
		x = x + e.target.offsetLeft;
		y = y + e.target.offsetTop;
	}
	var xWalk = Math.round(x / width * walk - walk / 2);
	var yWalk = Math.round(y / height * walk - walk / 2);
	text.style.textShadow = '\n\t  ' + xWalk + 'px ' + yWalk + 'px 0 rgba(255,0,255,0.7),\n\t  ' + xWalk * -1 + 'px ' + yWalk + 'px 0 rgba(0,255,255,0.7),\n\t  ' + yWalk + 'px ' + xWalk * -1 + 'px 0 rgba(0,255,0,0.7),\n\t  ' + yWalk * -1 + 'px ' + xWalk + 'px 0 rgba(0,0,255,0.7)\n\t';
}

hero.addEventListener('mousemove', shadow);