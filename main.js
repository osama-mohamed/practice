const form = document.querySelector('#add-cafe-form');


// saving data
form.addEventListener('submit', (e) => {
  e.preventDefault();
  db.collection('cafe').add({
      name: form.name.value,
      city: form.city.value
  });
  form.name.value = '';
  form.city.value = '';
});