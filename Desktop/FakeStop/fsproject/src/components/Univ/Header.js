 
import React, { Component } from 'react'
import Modal from "react-responsive-modal";
import { Link } from 'react-router-dom';
import appr from '../../config/firebase';
import { useHistory } from "react-router-dom";
 

export default function Header() {
 
 const  history =useHistory();
   
    
const handleClick= () =>{
appr.auth().signOut();
history.push('/');

}
    
 
        return (
        
            <header id="header">
         
            <nav class="navbar navbar-inverse" role="banner">
                <div class="container">
                    <div class="navbar-header">
                    <a class="navbar-brand" href="index.html"><img id="imf" src="images/f.png" alt="logo" /></a>
                        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                            <span class="sr-only">Toggle navigation</span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                        </button>
                       
                    </div>
    
                    <div class="collapse navbar-collapse navbar-right">
                        
                        <ul class="nav navbar-nav">
                        <li class="active"><Link to="/Univ">Add graduated </Link></li>
                            <li ><a onClick={handleClick}>Logout </a></li>
 
             
                            <space/>
                            <space/>
                          
                          
                          
                        
                        </ul>
                    </div>
                </div>
             
            </nav>
          
    
        </header>
      
    )
} 
