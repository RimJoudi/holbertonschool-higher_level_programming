import React from 'react'
import './login.css'
import {useForm}  from 'react-hook-form';
import { useHistory } from "react-router-dom";
import appr from '../../config/firebase';

export default function Singin() {
    const {register,handleSubmit, formState: { errors }} = useForm();
    const history=useHistory();
    const onSubmit = async(e,props) =>{
  
      try { 
          const user=  await appr.auth().signInWithEmailAndPassword(e.Uname1, e.pass1);    
            
            console.log(user.credential);
            history.push('/univ');
          } catch (error) {
            alert(error);
          }
       
      }
    return (
        <div class="form sign-in">
        <h2>Sign In</h2>
        <form  onSubmit={handleSubmit(onSubmit)}>
        <label>
          <span>Email</span>
          <input type="text" name="Uname1" {...register('Uname1')} />
        </label>
        <label>
          <span>Password</span>
          <input type="password" name="pass1" {...register('pass1')} /> 
        </label>
        <button type="submit"  id="sub" class="submit">Sign In</button>
        </form>
        <p class="forgot-pass"  >Forgot Password ?</p>
    </div>
    )
}
