
(function sayWelcome() {
    alert('welcome');
})();   // self invoke method 1


(function convertPrice() {
    var myPrice = document.getElementById('price').innerHTML;
    alert(myPrice * 3.75)
}());   // self invoke method 2


function convertDollar() {
    var amount = document.getElementById('dollar').value,
        result = amount * 20,
        message = document.getElementById('convert-result');
    if (amount === '') {
        message.innerHTML = 'This field can not be empty';
    } else if (isNaN(amount)) {
        message.innerHTML = 'This field accept numbers only';
    } else if (amount === '0') {
        message.innerHTML = 'Number can not be 0';
    } else if (amount < 0) {
        message.innerHTML = 'Number can not be less than 0';
    } else {
        message.innerHTML = amount + ' dollar is equal to ' + result + ' LE';
    }
}