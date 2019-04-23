// listen for auth status changes
auth.onAuthStateChanged(user => {
  if (user) {
    console.log('user logged in: ', user);
    // get data from db
    db.collection('guides').onSnapshot(snapshot => {
      setupGuides(snapshot.docs);
      setupUI(user);
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
  // toggle user elements
  if (user) {
    loggedInLinks.forEach(item => item.style.display = 'block');
    loggedOutLinks.forEach(item => item.style.display = 'none');
    // account info
    db.collection('users').doc(user.uid).get().then(doc => {
      accountDetails.innerHTML = `
        <div>Logged in as ${user.email}</div>
        <div>${doc.data().bio}</div>
      `;
    });
  } else {
    loggedInLinks.forEach(item => item.style.display = 'none');
    loggedOutLinks.forEach(item => item.style.display = 'block');
    // clear account info
    accountDetails.innerHTML = '';
  }
};