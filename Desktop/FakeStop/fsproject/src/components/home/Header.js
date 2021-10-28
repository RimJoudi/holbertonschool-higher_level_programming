 
import React, { Component } from 'react'
import Modal from "react-responsive-modal";
import { Link } from 'react-router-dom';


export default class Header extends Component {
   
    constructor(props) {
        super( )
 
        }
    

    


    render() {
        
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
                            <li class="active"><Link to="/home">Home </Link></li>
                         
                            <space/>
                            <space/>
                            <li>  <Link to="/Singup">Login/Singup </Link></li>
                          
                          
                        
                        </ul>
                    </div>
                </div>
             
            </nav>
          
    
        </header>
      
    )
} }
