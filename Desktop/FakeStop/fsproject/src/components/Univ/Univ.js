 
import './Univ.css'
import Header from './Header'
import React, { Component } from 'react'
import axios from 'axios';
export default class Univ extends Component {
  constructor(props) {
    super(props)
    this.ChangeHandler1=this.ChangeHandler1.bind(this);
    this.ChangeHandler2=this.ChangeHandler2.bind(this);
    this.ChangeHandler3=this.ChangeHandler3.bind(this);
    this.ChangeHandler4=this.ChangeHandler4.bind(this);
    this.ChangeHandler5=this.ChangeHandler5.bind(this);
    this.ChangeHandler6=this.ChangeHandler6.bind(this);
    this.ChangeHandler7=this.ChangeHandler7.bind(this);
    this.ChangeHandler8=this.ChangeHandler8.bind(this);
    this.state = {
      id:'',
      first_name:'',
      last_name:'',
      cin:'',
      birth_date:'',
      year:'',
      Diploma:'',
      school:''

    }
  }
  ChangeHandler1=(e)=>{
    this.setState({
      id:e.target.value,
    })
  }
  ChangeHandler2=(e)=>{
    this.setState({
      first_name:e.target.value,
    })
  }
  ChangeHandler3=(e)=>{
    this.setState({
      last_name:e.target.value,
    })
  }
  ChangeHandler4=(e)=>{
    this.setState({
      cin:e.target.value,
    })
  }
  ChangeHandler5=(e)=>{
    this.setState({
      birth_date:e.target.value,
    })
  }
  ChangeHandler7=(e)=>{
    this.setState({
      Diploma:e.target.value,
    })
  }
  ChangeHandler6=(e)=>{
    this.setState({
      year:e.target.value,
    })
  }
  ChangeHandler8=(e)=>{
    this.setState({
      school:e.target.value,
    })
  }
 
 
  submitHandler=async(e)=>{e.preventDefault()
  try{  const Data = {
      first_name:this.state.first_name,
      last_name:this.state.last_name,
      cin:this.state.cin,
      birth_date:this.state.birth_date,
      year:this.state.year,
      Diploma:this.state.Diploma,
      school:this.state.school,
    }
  console.log(Data);
 await axios.post('http://localhost:8000/process_post', Data)
  .then((res) => {
      console.log(res.data)
  }).catch((error) => {
      console.log(error)
  });}
catch(err){
  console.log(err);
}}
  render() {
     
    return (<div>
      <Header/>
          <section id="h">
      <div class="container">
 
   
        <div class="row justify-content-center">
          <div class="col-12 col-md-8 col-lg-8 col-xl-6">
            <div class="row">
              <div class="col text-center">
                <h1>Add new graduated</h1>
                <p class="text-h3">Far far away, behind the word mountains, far from the countries Vokalia and Consonantia. </p>
              </div>
            </div>
            <form onSubmit={this.submitHandler}>
            <div class="row align-items-center">
              <div class="col mt-4">
                <input type="text" class="form-control" placeholder="id" value={this.state.id} onChange={this.ChangeHandler1} />
              </div>
            </div>
            <div class="row align-items-center mt-4">
              <div class="col">
                <input type="text" class="form-control" name="first_name" placeholder="Given_name" value={this.state.first_name} onChange={this.ChangeHandler2}/>
              </div>
            </div>
            <div class="row align-items-center mt-4">
              <div class="col">
                <input type="text" class="form-control" name="last_name" placeholder="Family_name" value={this.state.last_name} onChange={this.ChangeHandler3}/>
              </div>
              <div class="col">
                <input type="text" class="form-control" name="cin" placeholder="National_identification_number" 
                value={this.state.cin} onChange={this.ChangeHandler4}/>
              </div>
              <div class="col">
                <input type="date" class="form-control" name="birth_date" placeholder="Date_of_birth"
                value={this.state.birth_date} onChange={this.ChangeHandler5}/>
              </div>
              {/* <div class="col">
                <input type="text" class="form-control" name="Scientific_discipline" placeholder="Scientific_discipline"/>
              </div> */}
              <div class="col">
                <input type="date" class="form-control" name="year" 
                placeholder="Diploma_issue_date" value={this.state.year} onChange={this.ChangeHandler6}/>
              </div>
              <div class="col">
                <input type="text" class="form-control" 
                name="Diploma" placeholder="Scientific_discipline" value={this.state.Diploma} onChange={this.ChangeHandler7}/>
              </div>
              <div class="col">
                <input type="text" class="form-control" name="school" placeholder="Diploma_issued_by"
                value={this.state.school} onChange={this.ChangeHandler8}/>
              </div>
            </div>
            <div class="row justify-content-start mt-4">
  
                <button class="btn btn-primary mt-4">Submit</button>

            </div>
            </form>
          </div>
        </div>
      </div>
    </section></div>
      )
  }
}

 