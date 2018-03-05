
var myOldPrice = 1000,
    myNewPrice = 100,
    myDiscount = myOldPrice - myNewPrice + 50;

document.getElementById('price').innerHTML = myDiscount;


var mainPrice = 500,
    mySmallDiscount = 50,
    myMediumDiscount = 100,
    myBigDiscount = 250;

document.getElementById('main-price').innerHTML = mainPrice;
document.getElementById('product1').innerHTML = mainPrice - mySmallDiscount;
document.getElementById('product2').innerHTML = mainPrice - myMediumDiscount;
document.getElementById('product3').innerHTML = mainPrice - myBigDiscount;
