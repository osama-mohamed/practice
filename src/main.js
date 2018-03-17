
var myPromise = Promise.resolve('Yeah');
myPromise.then((res) => console.log(res));
// myPromise.then(function(res) {console.log(res)});


var myPromise2 = new Promise(function (resolve, reject) {
	console.log('Wait 2 seconds!');
	setTimeout(() => resolve(4), 2000);
});

myPromise2.then((res) => {
	res += 3;
	console.log(res);
});


function getData(method, url) {
	return new Promise(function (resolve, reject) {
		var xhr = new XMLHttpRequest();
		xhr.open(method, url);
		xhr.onload = function () {
			if (this.status >= 200 && this.status < 300) {
				resolve(xhr.response);
			} else {
				reject({
					status: this.status,
					statusText: xhr.statusText
				});
			}
		};
		xhr.onerror = function () {
			reject({
				status: this.status,
				statusText: xhr.statusText
			});
		};
		xhr.send();
	});
}

getData('GET', 'https://api.github.com/users').then(function (data) {
	console.log(data);
	let todos = JSON.parse(data);
	let output = '';
	for (let todo of todos) {
		output += `
			<div>
				<h3>Username : ${todo.login}</h3>
				<p>URL : <a href="${todo.url}" target="_blank">${todo.url}</a></p>
			</div>
		`;
	}
	document.getElementById('test').innerHTML = output;
}).catch(function (err) {
	console.log(err);
});