import React from 'react';
import './App.css';
import Navbar from './components/Navbar'
import Contact from './components/Contact'

function App() {
  
  return (
    <div className="App">
      <Navbar isAuthenticated={false}/>
      <div className="container">
      <h1 className="text-center">Hello World</h1>
      <p className="center" style={{ color: '#FF0000' }}>Salam Dunya</p>
      <Contact/>
      </div>
    </div>
  );
}

export default App;
