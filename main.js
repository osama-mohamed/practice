
var newCar = {
    color: 'black',
    type: 'sedan',
    model: 2018
},
    prop;

for (prop in newCar) {
    if (newCar.hasOwnProperty(prop)) {
        console.log(prop + " : " + newCar[prop])
    }
}
