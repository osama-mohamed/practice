// signup
const signupForm = document.querySelector('#signup-form');
signupForm.addEventListener('submit', (e) => {
  e.preventDefault();
  // get user info
  const email = signupForm['signup-email'].value;
  const password = signupForm['signup-password'].value;
  // sign up the user & add firestore data
  auth.createUserWithEmailAndPassword(email, password).then(cred => {
    return db.collection('users').doc(cred.user.uid).set({
      bio: signupForm['signup-bio'].value
    });
  }).then(() => {
    // close the signup modal & reset form
    const modal = document.querySelector('#modal-signup');
    M.Modal.getInstance(modal).close();
    signupForm.reset();
    signupForm.querySelector('.error').innerHTML = '';
  }).catch(err => {
    signupForm.querySelector('.error').innerHTML = err.message;
  });
});


// login
const loginForm = document.querySelector('#login-form');
loginForm.addEventListener('submit', (e) => {
  e.preventDefault();
  // get user info
  const email = loginForm['login-email'].value;
  const password = loginForm['login-password'].value;
  // log the user in
  auth.signInWithEmailAndPassword(email, password).then((cred) => {
    console.log(cred.user.email, cred.user.uid);
    // close the signup modal & reset form
    const modal = document.querySelector('#modal-login');
    M.Modal.getInstance(modal).close();
    loginForm.reset();
    loginForm.querySelector('.error').innerHTML = '';
  }).catch(err => {
    loginForm.querySelector('.error').innerHTML = err.message;
  });
});


// logout
const logout = document.querySelector('#logout');
logout.addEventListener('click', (e) => {
  e.preventDefault();
  auth.signOut().then(() => {
    console.log('user signed out');
  });
});
