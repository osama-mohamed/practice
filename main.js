
var x = 1;

function xParent() {
    var x = 2;
    var cal = x + 2;
    function xTest() {
        var x = 5,
            cal = x + 2;
        console.log(cal);
    }
    return xTest();
}

console.log(x);
xParent();
console.log(x);


