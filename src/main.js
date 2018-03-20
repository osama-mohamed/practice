const divs = document.querySelectorAll('div');
const button = document.querySelector('button');

function logText(e) {
  console.log(this.classList.value);
  // e.stopPropagation(); // stop bubbling!
}

divs.forEach(div => div.addEventListener('click', logText, {
  // capture: true, // from root to top
  capture: false,   // from top to root
  once: true        // run only one time, don not repeat
}));

button.addEventListener('click', () => {
  console.log('you click the button');
}, {
  once: true
});
