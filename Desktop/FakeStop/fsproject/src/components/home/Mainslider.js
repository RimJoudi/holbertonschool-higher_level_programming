import React from 'react'
import { useHistory } from "react-router-dom";
export default function Mainslider() {
    const  history =useHistory();
    const handleClick= () =>{
        
        history.push('/verif');
        
        }
         
    return (
      
    <section id="main-slider" class="no-margin">
    <div class="carousel slide">
      
        <div class="carousel-inner">

            <div class="item active"  >
                <div class="container">
                    <div class="row">
                        <div class="col-md-7">
                            <div class="carousel-content">
                                <h1 class="animation animated-item-1">FakeStop</h1>
                                <div class="animation animated-item-2">
                                    Every new computer that’s brought home from the store has an operating system installed onto it.
                                </div>
                                <a class="btn-slide animation animated-item-3" href="#">Learn More</a>
                                <a class="btn-slide white animation animated-item-3" onClick={handleClick}>Get Started</a>
                            </div>
                        </div>

                    </div>
                </div>
            </div> 

            <div class="item">
                <div class="container">
                    <div class="row">
                        <div class="col-md-7">
                            <div class="carousel-content">
                                <h1 class="animation animated-item-1">FakeStop</h1>
                                <div class="animation animated-item-2">
                                    Every new computer that’s brought home from the store has an operating system installed onto it.
                                </div>
                    
                                <a class="btn-slide animation animated-item-3" href="#">Get Started</a>
                            </div>
                        </div>


                    </div>
                </div>
            </div>
   

        </div>
 
    </div>
    
</section>
    )
}
