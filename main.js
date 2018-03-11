
var myElement = document.getElementById('myImg'),
    myImgs = [
        'img/js.png',
        'img/python2.png',
        'img/mysql.png',
        'img/mariadb.png',
        'img/5.png',
        'img/CSS33.png'
    ];


function changeImg(myElement, myImgs) {
    setInterval(function () {
        var myRandomNumber = Math.floor(Math.random() * myImgs.length)
        myElement.src = myImgs[myRandomNumber];
        console.log(myRandomNumber);
        console.log(myImgs[myRandomNumber]);
    }, 1000);
}
changeImg(myElement, myImgs);

