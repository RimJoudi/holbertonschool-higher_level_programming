 
import Header from '../home/Header'
import '../Univ/Univ.css'
import axios from 'axios';
import React, { Component } from 'react'

export default class Verif extends Component {
  constructor(props) {
    super(props)
    this.ChangeHandler=this.ChangeHandler.bind(this);
    this.state = {
      cin:'',
    }
  }
  ChangeHandler=(e)=>{
    this.setState({
      cin:e.target.value,
    })
  }
  
  submitHandlerr=e=>{e.preventDefault()
    const Data = {
      cin:this.state.cin,
    }
  console.log(Data);
  axios.post('http://localhost:8000/verify_post', Data)
  .then((res) => {
      console.log(res.data)
  }).catch((error) => {
      console.log(error)
  });}
  render() {
    return (<div>
      <Header />
      <section id="h2">
  <div class="container">


    <div class="row justify-content-center">
      <div class="col-12 col-md-8 col-lg-8 col-xl-6">
        <div class="row">
          <div class="col text-center">
            <h1>Add new graduated</h1>
            <br/>
            <p class="text-h3">Far far away, behind the word mountains, far from the countries Vokalia and Consonantia. </p>
          </div>
          </div>
          <form onSubmit={this.submitHandlerr}> 
                <div class="row align-items-center">
                  <div class="col mt-4">
                    <input type="text" class="form-control" placeholder="id"
                    value={this.state.cin} onChange={this.ChangeHandler}  />
                  </div>
                </div>
                
                <div class="row justify-content-start mt-4">
                  <div class="col">
                    
                
                  <button class="btn btn-primary mt-4">Check</button>
                  </div>
                </div>
          </form>   
      </div>
    </div>
  </div>
</section></div>
  )
  }
}

 