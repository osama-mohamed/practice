// listen for auth status changes
auth.onAuthStateChanged(user => {
  if (user) {
    console.log('user logged in: ', user);
    user.getIdTokenResult().then(idTokenResult => {
      console.log(idTokenResult.claims);
      user.admin = idTokenResult.claims.admin;
      setupUI(user);
    });
    // get data from db
    db.collection('guides').onSnapshot(snapshot => {
      setupGuides(snapshot.docs);
    }, err => console.log(err.message));
  } else {
    console.log('user logged out');
    setupGuides([]);
    setupUI();
  }
});


const setupUI = (user) => {
  const loggedOutLinks = document.querySelectorAll('.logged-out');
  const loggedInLinks = document.querySelectorAll('.logged-in');
  const accountDetails = document.querySelector('.account-details');
  const adminItems = document.querySelectorAll('.admin');
  // toggle user elements
  if (user) {
    if (user.admin) {
      adminItems.forEach(item => item.style.display = 'block');
    }
    loggedInLinks.forEach(item => item.style.display = 'block');
    loggedOutLinks.forEach(item => item.style.display = 'none');
    // account info
    db.collection('users').doc(user.uid).get().then(doc => {
      accountDetails.innerHTML = `
        <div>Logged in as ${user.email}</div>
        <div>${doc.data().bio}</div>
        <div class="pink-text">${user.admin ? 'Admin' : ''}</div>
      `;
    });
  } else {
    adminItems.forEach(item => item.style.display = 'none');
    loggedInLinks.forEach(item => item.style.display = 'none');
    loggedOutLinks.forEach(item => item.style.display = 'block');
    // clear account info
    accountDetails.innerHTML = '';
  }
};