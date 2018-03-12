/*
	window.open(
	url,
	tab-name or target-attribute(_blank[default], _self, ..),
	specification,
	history replace (true or false)
	)
*/


document.getElementById('click').onclick = function () {
	window.open(
		'https://www.google.com.eg',
		'OSAMA MOHAMED',
		'width=600, height=400, left=500, top=100, menubar=yes, status=no',
		'true'
	);
};