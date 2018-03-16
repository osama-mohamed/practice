

let name = 'OSAMA';

function makeUpperCase(word) {
	return word.toUpperCase();
}

let text = `<h1>${makeUpperCase('Hello')} ${name}</h1>
			<p>This is a paragraph</p>`;

document.getElementById('test').innerHTML = text;