 
import './login.css' 
 
import React,{useEffect,useState} from 'react'
import {useForm}  from 'react-hook-form';
import appr from '../../config/firebase';
import Header from '../home/Header';
import Singin from './Singin';


export default function Singup() {
  const {register,handleSubmit, formState: { errors }} = useForm();

  useEffect(() => {
     
   document.querySelector('.img-btn').addEventListener('click', function()
   {
     document.querySelector('.cont').classList.toggle('s-signup')
   });
  });
const [currentUser, setCurrentUser] = useState(null);    
 

  const onSubmit = (e)=>{
    console.log(e)
    alert(e.Uname)
        
      try { 
        appr.auth().createUserWithEmailAndPassword(e.email, e.pass);    
   
        setCurrentUser(true);
      } catch (error) {
        alert(error);
      }
   
  }

  const onLogin = async(e)=>{
  console(e)
  }
      
    return (<div>
    <Header />
    <div id="body"> 
      <div class="cont">
      <Singin />
    
        <div class="sub-cont"  >
          <div class="img">
            <div class="img-text m-up">
              <h2>New here?</h2>
              <p>Sign up and discover great amount of new opportunities!</p>
            </div>
            <div class="img-text m-in">
              <h2>One of us?</h2>
              <p>If you already has an account, just sign in. We've missed you!</p>
            </div>
            <div class="img-btn">
              <span class="m-up">Sign Up</span>
              <span class="m-in">Sign In</span>
            </div>
          </div>
          <div class="form sign-up">
            <h2>Sign Up</h2>
            <form onSubmit={handleSubmit(onSubmit)}>
            <label>
              <span>UserName</span>
              <input type="text"  name="Uname" {...register('Uname', { required: true,minLength:4 })} />
              {errors.Uname && <p id="err">At least 4 characters</p>}
            </label>
            <label>
              <span>Email</span>
              <input type="email" name="email" {...register('email', { required: true })}  />
              {errors.email && <p id="err">u have enter an @ account</p>}
            </label>
            <label>
              <span>Password</span>
              <input type="password" name="pass" {...register('pass', { required: true ,minLength:5})} />
              {errors.pass && <p id="err">At least 5 characters</p>}
            </label>
            <label>
              <span>Confirm Password</span>
              <input type="password" name="cpass" {...register('cpass', { required: true, minLength:5 })} />
              {errors.cpass && <p id="err">At least 5 characters</p>}
            </label>
            
  
            <button type="submit"  id="sub" class="submit">Sign Up Now</button>
            </form>
           </div> 
      
          </div>
          </div>
  </div></div>
    )
    
}
 
