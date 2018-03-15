
var x = 1,
	y = 1;
while (x <= 12) {
	while (y <= 12) {
		console.log(x + ' * ' + y + ' = ' + x*y);
		y += 1;
	}
	console.log('*************');
	y = 1;
	x += 1;
}

