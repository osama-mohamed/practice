
var myTitle = document.getElementById('title'),
    myContent = document.getElementById('content'),
    myLiveTitle = document.getElementById('title-live'),
    myLiveContent = document.getElementById('content-live');

function livePreview(i1, i2) {
    i1.onkeyup = function () {
        i2.textContent = this.value;
    };
}

livePreview(myTitle, myLiveTitle);
livePreview(myContent, myLiveContent);
