import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

const firebaseConfig = {
  apiKey: "AIzaSyCnCcU0t2naj59OC_cQ-MFgLFuHNMr9uek",
  authDomain: "reliabilityiq.firebaseapp.com",
  projectId: "reliabilityiq",
  storageBucket: "reliabilityiq.appspot.com",
  messagingSenderId: "104501551043",
  appId: "1:104501551043:web:7ef9bed841151eafefe776",
  measurementId: "G-N2M5E7Q133"
};

const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

export default app;

