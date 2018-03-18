'use strict';

var addItems = document.querySelector('.add-items');
var itemsList = document.querySelector('.plates');
var items = JSON.parse(localStorage.getItem('items')) || [];
var checkAll = document.querySelector('.check-all');
var uncheckAll = document.querySelector('.uncheck-all');
var deleteAll = document.querySelector('.delete-all');

function addItem(e) {
	e.preventDefault();
	var text = this.querySelector('[name=item]').value;
	var item = {
		text: text,
		done: false
	};
	items.push(item);
	populateList(items, itemsList);
	localStorage.setItem('items', JSON.stringify(items));
	this.reset();
}

function populateList() {
	var plates = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : [];
	var platesList = arguments[1];

	platesList.innerHTML = plates.map(function (plate, i) {
		return '\n\t\t\t<li>\n\t\t\t  <input type="checkbox" data-index=' + i + ' id="item' + i + '" ' + (plate.done ? 'checked' : '') + ' />\n\t\t\t  <label for="item' + i + '">' + plate.text + '</label>\n\t\t\t</li>\n\t\t';
	}).join('');
}

function toggleDone(e) {
	if (!e.target.matches('input')) return;
	var el = e.target;
	var index = el.dataset.index;
	items[index].done = !items[index].done;
	localStorage.setItem('items', JSON.stringify(items));
	populateList(items, itemsList);
}

function checkAllInputs() {
	var i = 0;
	for (; i < items.length; i += 1) {
		items[i].done = true;
	}
	localStorage.setItem('items', JSON.stringify(items));
	populateList(items, itemsList);
}

function uncheckAllInputs() {
	var i = 0;
	for (; i < items.length; i += 1) {
		items[i].done = false;
	}
	localStorage.setItem('items', JSON.stringify(items));
	populateList(items, itemsList);
}

function deleteAllInputs() {
	localStorage.removeItem('items');
	itemsList.innerHTML = '';
	items = [];
}

addItems.addEventListener('submit', addItem);
itemsList.addEventListener('click', toggleDone);
checkAll.addEventListener('click', checkAllInputs);
uncheckAll.addEventListener('click', uncheckAllInputs);
deleteAll.addEventListener('click', deleteAllInputs);

populateList(items, itemsList);