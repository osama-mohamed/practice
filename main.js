

var myButton = document.getElementById('top');

window.onscroll = function () {
    if (window.pageYOffset >= 600){
        myButton.style.display = 'block';
    } else {
        myButton.style.display = 'none';
    }
};

myButton.onclick = function () {
    window.scrollTo(0, 0);
};