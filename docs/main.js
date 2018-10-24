const cafeList = document.querySelector("#cafe-list");
const form = document.querySelector("#add-cafe-form");

// create element & render cafe
function renderCafe(doc) {
  let li = document.createElement("li");
  let name = document.createElement("span");
  let city = document.createElement("span");
  let cross = document.createElement("div");

  li.setAttribute("data-id", doc.id);
  name.textContent = doc.data().name;
  city.textContent = doc.data().city;
  cross.textContent = "x";

  li.appendChild(name);
  li.appendChild(city);
  li.appendChild(cross);
  cafeList.appendChild(li);
  // deleting data
  cross.addEventListener('click', deleteCafe);

}

function deleteCafe(e) {
  e.stopPropagation();
  let id = e.target.parentElement.getAttribute("data-id");
  db.collection("cafe").doc(id).delete();
  e.target.parentElement.remove();
}

// saving data
form.addEventListener("submit", e => {
  if(form.name.value == '' || form.city.value == '') {
    alert('You must enter a cafe name and cafe city');
    return false;
  }
  e.preventDefault();
  db.collection("cafe").add({
    name: form.name.value,
    city: form.city.value
  });
  form.name.value = "";
  form.city.value = "";
});

// real-time listener
db.collection("cafe")
  .orderBy("city")
  .onSnapshot(snapshot => {
    let changes = snapshot.docChanges();
    changes.forEach(change => {
      if (change.type == "added") {
        renderCafe(change.doc);
      } else if (change.type == "removed") {
        console.log('deleted one cafe successfully');
      }
    });
  });


// getting data
// db.collection('cafe').get().then(snapshot => {
//   snapshot.docs.forEach(doc => {
//     renderCafe(doc);
//   });
// });