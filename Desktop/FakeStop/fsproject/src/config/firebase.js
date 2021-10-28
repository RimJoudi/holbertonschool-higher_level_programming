import firebase from 'firebase'
require('firebase/auth')
require('firebase/firestore')
const firebaseConfig = {
    apiKey: "AIzaSyC7TcCi10GrdKYngOeNSz0vMg4vgrSgjNk",
    authDomain: "reactrp-89fa1.firebaseapp.com",
    databaseURL: "https://reactrp-89fa1-default-rtdb.europe-west1.firebasedatabase.app",
    projectId: "reactrp-89fa1",
    storageBucket: "reactrp-89fa1.appspot.com",
    messagingSenderId: "168453797994",
    appId: "1:168453797994:web:1d5a9cb3a4afd92242b213",
    measurementId: "G-FWV8KFSE72"
  };
const appr = firebase.initializeApp(firebaseConfig);
 
export default appr;
 //firebase@8.10.0//