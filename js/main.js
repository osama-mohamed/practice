const APIKEY = "86422a8278fea6af679b768074ccf0ee";
const URL = "http://api.petfinder.com/";

import fetchJsonp from "fetch-jsonp";
import { isValidZip, showAlert } from "./validate";

const petForm = document.querySelector("#pet-form");

petForm.addEventListener("submit", fetchAnimals);

function fetchAnimals(e) {
  e.preventDefault();
  const animal = document.querySelector("#animal").value;
  const zip = document.querySelector("#zip").value;
  document.querySelector('#results').innerHTML = '';
  if(!isValidZip(zip)) {
    showAlert('Please Enter A valid Zip Code!', 'alert-danger');
    return false;
  }

  fetchJsonp(
    `${URL}pet.find?format=json&key=${APIKEY}&animal=${animal}&location=${zip}&count=25&callback=callback`,
    {
      jsonpCallbackFunction: "callback"
    }
  )
    .then(res => res.json())
    .then(data => showAnimals(data.petfinder.pets.pet))
    .catch(err => console.log(err));
}

function showAnimals(pets) {
  const results = document.querySelector('#results');
  results.innerHTML = '';
  pets.forEach((pet) => {
    const div = document.createElement('div');
    div.classList.add('card', 'card-body', 'mb-3');
    div.innerHTML = `
    <div class="row">
      <div class="col-sm-6">
        <h4>${pet.name.$t} (${pet.age.$t})</h4>
        <p class="text-secondary">${pet.breeds.breed.$t}</p>
        <p>${pet.contact.address1.$t} - ${pet.contact.city.$t} - ${pet.contact.state.$t} - ${pet.contact.zip.$t}</p>
        <ul class="list-group">
          ${pet.contact.phone.$t ? `<li class="list-group-item">Phone: ${pet.contact.phone.$t}</li>` : ``}
          ${pet.contact.email.$t ? `<li class="list-group-item">E-mail: ${pet.contact.email.$t}</li>` : ``}
          ${pet.shelterId.$t ? `<li class="list-group-item">Shelter ID: ${pet.shelterId.$t}</li>` : ``}
          ${pet.sex.$t ? `<li class="list-group-item">Sex: ${pet.sex.$t}</li>` : ``}
        </ul>
      </div>
      <div class="col-sm-6 text-center">
      ${pet.media.photos.photo[3].$t ? `<img src="${pet.media.photos.photo[3].$t}" class="img-fluid rounded-circle mt-2">` : ``}
      </div>
    </div>`;
    results.appendChild(div);
  });
}
