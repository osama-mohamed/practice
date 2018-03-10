
var newCar = {
    color: 'black',
    type: 'sedan',
    model: 2018
},
    prop;

console.log(newCar);
console.log(newCar.model);
console.log(newCar['model']);


for (prop in newCar) {
    if (newCar.hasOwnProperty(prop)) {
        console.log(prop + " : " + newCar[prop])
    }
}