
var myTitle = document.getElementById('title'),
    myContent = document.getElementById('content'),
    myLiveTitle = document.getElementById('title-live'),
    myLiveContent = document.getElementById('content-live');

myTitle.onkeyup = function () {
    myLiveTitle.textContent = this.value;
};

myContent.onkeyup = function () {
    myLiveContent.textContent = this.value;
};
