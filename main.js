
var number1 = prompt('Enter your first number : '),
	number2 = prompt('Enter your second number : '),
	number3 = prompt('Enter your third number : ');

function numbers(num1, num2, num3) {
	var x ,
		y,
		z;
	for(x = 0; x <= num1; x += 1) {
		for(y = 0; y <= num2; y += 1) {
			for(z = 0; z <= num3; z += 1) {
				console.log(x, y, z);
			}
		}
	}
}

numbers(parseInt(number1), parseInt(number2), parseInt(number3));
