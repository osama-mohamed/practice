const addItems = document.querySelector('.add-items');
const itemsList = document.querySelector('.plates');
let items = JSON.parse(localStorage.getItem('items')) || [];
const checkAll = document.querySelector('.check-all');
const uncheckAll = document.querySelector('.uncheck-all');
const deleteAll = document.querySelector('.delete-all');


function addItem(e) {
	e.preventDefault();
	const text = (this.querySelector('[name=item]')).value;
	const item = {
		text,
		done: false
	};
	items.push(item);
	populateList(items, itemsList);
	localStorage.setItem('items', JSON.stringify(items));
	this.reset();
}

function populateList(plates = [], platesList) {
	platesList.innerHTML = plates.map((plate, i) => {
		return `
			<li>
			  <input type="checkbox" data-index=${i} id="item${i}" ${plate.done ? 'checked' : ''} />
			  <label for="item${i}">${plate.text}</label>
			</li>
		`;
	}).join('');
}

function toggleDone(e) {
	if (!e.target.matches('input')) return;
	const el = e.target;
	const index = el.dataset.index;
	items[index].done = !items[index].done;
	localStorage.setItem('items', JSON.stringify(items));
	populateList(items, itemsList);
}

function checkAllInputs() {
	let i = 0;
	for (; i < items.length; i += 1) {
		items[i].done = true;
	}
	localStorage.setItem('items', JSON.stringify(items));
	populateList(items, itemsList);
}

function uncheckAllInputs() {
	let i = 0;
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
