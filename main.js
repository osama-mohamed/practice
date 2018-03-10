

var myInput = document.getElementById('my-input');

myInput.onfocus = function () {
    this.setAttribute('data-place', this.getAttribute('placeholder'));
    this.setAttribute('placeholder', '');
};

myInput.onblur = function () {
    this.setAttribute('placeholder', this.getAttribute('data-place'));
    this.setAttribute('data-place', '');
};
