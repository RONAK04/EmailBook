//src/App.js
import { Component } from 'react';
import {
  Form,
  FormFeedback,
  FormGroup,
  FormText,
  Label,
  Input,
  
} from 'reactstrap';
import './App.css';
 
class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      email: '',
      password: '',
      validate: {
        emailState: '',
      },
    };
    this.handleChange = this.handleChange.bind(this);
  }
 
  handleChange = (event) => {
    const { target } = event;
    const value = target.type === 'checkbox' ? target.checked : target.value;
    const { name } = target;
 
    this.setState({
      [name]: value,
    });
  };
 
  validateEmail(e) {
    const emailRex =
      /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
 
    const { validate } = this.state;
 
    if (emailRex.test(e.target.value)) {
      validate.emailState = 'has-success';
    } else {
      validate.emailState = 'has-danger';
    }
 
    this.setState({ validate });
  }
 
  submitForm(e) {
    e.preventDefault();
    console.log(`Email: ${this.state.email}`);
  }
 
  render() {
    const { email, password } = this.state;
 
    return (
      <div className="App">
        <h2>Mail Book</h2>
        <p>Please Enter Your Login Id and Password!</p>
        <Form className="form" onSubmit={(e) => this.submitForm(e)}>
          <FormGroup>
            <Label>Username</Label>
            <Input
              type="email"
              name="email"
              id="exampleEmail"
              placeholder="example@example.com"
              valid={this.state.validate.emailState === "has-success"}
              invalid={this.state.validate.emailState === "has-danger"}
              value={email}
              onChange={(e) => {
                this.validateEmail(e);
                this.handleChange(e);
              }}
            />
            <FormFeedback>
              Uh oh! Looks like there is an issue with your email. Please input
              a correct email.
            </FormFeedback>
            <FormFeedback valid>
              That's a tasty looking email you've got there.
            </FormFeedback>
            <FormText>Your username is most likely your email.</FormText>
          </FormGroup>
          <FormGroup>
            <Label for="examplePassword">Password</Label>
            <Input
              type="password"
              name="password"
              id="examplePassword"
              placeholder="********"
              value={password}
              onChange={(e) => this.handleChange(e)}
            /><br/>
            <a href=''>Forgot Password?</a>
          </FormGroup> 
          <div class="d-grid">
          <button type='submit' class='btn btn-primary' >Submit</button>
          </div>
        </Form>
        <div class="mt-3">
          <p class="mb-0 text-center">Don't have an account? <a href='' class="text-primary fw-bold">Sign Up</a></p>
          </div>
      </div>
    );
  }
}
 
export default App;