 
import './App.css';
import React from 'react'
 
 import Home from './components/home/Home';
import { BrowserRouter as Router,Switch, Route } from 'react-router-dom';
import Header from './components/home/Header';
import Singup from './components/login/Singup';
import Univ from './components/Univ/Univ';
import Verif from './components/verif/Verif';

export const App  = () => {
  
  return (
     <div className="App">
    
      <Router>
     
        <Switch>
      <Route path="/Verif" component={Verif} />
     <Route path="/Singup" component={Singup}/>
     <Route path="/Univ" component={Univ}/>
        <Route path="/" component={Home} /> 
        </Switch>
  

       </Router>

     </div>
   )
 }
 

export default App;
