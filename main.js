
var number1 = prompt('Enter your first number : '),
	number2 = prompt('Enter your second number : '),
	number3 = prompt('Enter your third number : ');

function numbers(num1, num2, num3) {
	var x = 0,
		y = 0,
		z = 0;
	while (x <= num1) {
		while (y <= num2) {
			while (z <= num3) {
				console.log(x, y, z);
				z += 1;
			}
			z = 0;
			y += 1;
		}
		y = 0;
		x += 1;
	}
}

numbers(parseInt(number1), parseInt(number2), parseInt(number3));
