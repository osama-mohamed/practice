// get data from db
db.collection('guides').get().then(snapshot => {
  setupGuides(snapshot.docs);
});


// setup guides
const setupGuides = (data) => {
  const guideList = document.querySelector('.guides');
  let html = '';
  data.forEach(doc => {
    const guide = doc.data();
    const li = `
      <li>
        <div class="collapsible-header grey lighten-4"> ${guide.title} </div>
        <div class="collapsible-body white"> ${guide.content} </div>
      </li>
    `;
    html += li;
  });
  guideList.innerHTML = html;
};
