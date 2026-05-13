import { initializeApp } from 'firebase/app'
import { getAuth, GoogleAuthProvider } from 'firebase/auth'
import { getFirestore } from 'firebase/firestore'

const firebaseConfig = {
  apiKey: 'AIzaSyCTpJUFSA9OqWIKtrQPd6lWZ79x1GAOifc',
  authDomain: 'presupuesto-familiar-15478.firebaseapp.com',
  databaseURL: 'https://presupuesto-familiar-15478-default-rtdb.firebaseio.com',
  projectId: 'presupuesto-familiar-15478',
  storageBucket: 'presupuesto-familiar-15478.firebasestorage.app',
  messagingSenderId: '436445257047',
  appId: '1:436445257047:web:7078cb4a037c4eeb7c3212',
  measurementId: 'G-PVZD60T03P',
}

const app = initializeApp(firebaseConfig)
export const auth = getAuth(app)
export const db = getFirestore(app)
export const googleProvider = new GoogleAuthProvider()
