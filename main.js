

function generateSerial() {
    var chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        serialLength = 20,
        randomSerial = '',
        randomNumber,
        i = 0;
    for (; i < serialLength; i += 1) {
        randomNumber = Math.floor(Math.random() * chars.length);
        randomSerial += chars.substring(randomNumber, randomNumber + 1);
    }
    document.getElementById('serial').innerHTML = randomSerial;
}
