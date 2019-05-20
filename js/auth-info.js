// Initialize Firebase
const config = {
  apiKey: "AIzaSyDPxwbN194tRhlDOMhkyVttVaQJe_bXBaM",
  authDomain: "gameguidez-6.firebaseapp.com",
  databaseURL: "https://gameguidez-6.firebaseio.com",
  projectId: "gameguidez-6",
  storageBucket: "gameguidez-6.appspot.com",
  messagingSenderId: "991247981309"
};
firebase.initializeApp(config);

// make auth and firestore references
const auth = firebase.auth();
const db = firebase.firestore();
const functions = firebase.functions();
// update firestore settings
db.settings({ timestampsInSnapshots: true });
