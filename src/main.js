
function sayHello($hello = 'Hello OSAMA MOHAMED') {
	console.log($hello);
}

sayHello();        // > returns the default value which is Hello OSAMA MOHAMED
sayHello('Ahmed'); // > returns Ahmed





let num1 = [1, 2, 3],
	num2 = [4, 5, 6];

function concatNums() {
	console.log(num1 + ',' + num2);
}

concatNums(...num1, ...num2);