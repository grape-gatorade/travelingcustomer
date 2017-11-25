import React, { Component } from 'react';
import { FormGroup, FormControl, ControlLabel, Form } from 'react-bootstrap';
import styles from '../CSS/Thumbnail.css';

/*
Generate a list of numbers
param = Integer
*/
class DropdownTime extends Component {
  static populateList(Num) {
    console.log('populate ', Num);
    let i = 0;
    const x = [];
    for (i; i < parseInt(Num, 10); i += 1) {
      // console.log('for: ', i);
      let num = i;
      if (i < 10) {
        num = '0'.concat(i);
      }
      x.push(num);
    }
    return x;
  }
  /* Creates a drop down time selection component */
  constructor(props) {
    super(props);
    this.state = {
      hour: null,
      minute: null,
    }
    this.handleSelectHour = this.handleSelectHour.bind(this);
    this.handleSelectMinute = this.handleSelectMinute.bind(this);
  }
  /* Updates the state hour variable */
  handleSelectHour(event) {
    console.log('handleSelectHour', event.target.value);
    this.setState({ hour: event.target.value });
  }
  handleSelectMinute(event) {
    console.log('handleSelectMinute', event.target.value);
    this.setState({ minute: event.target.value });
  }
  // { { horas }.map(item => (
  //   <option>{item}</option>
  // ))}
  render() {
    // this.populateList(16);
    const horas = this.constructor.populateList(12);
    const minutos = this.constructor.populateList(60);
    return (
      <Form inline>
        <FormGroup controlId="formControlsSelect">
          <ControlLabel>Select {this.props.spec} :</ControlLabel>
          <FormControl
            componentClass="select"
            onChange={this.handleSelectHour}
            placeholder="select"
          >
            <option> Select Hour </option>
            {horas.map(num => (<option key={num}> { num } </option>))}
          </FormControl>
          :
          <FormControl
            componentClass="select"
            placeholder="select"
            onChange={this.handleSelectMinute}
          >
            <option> Select Minutes </option>
            {minutos.map(num => (<option key={num}> { num } </option>))}
          </FormControl>
          <FormControl componentClass="select" placeholder="select">
            <option>AM</option>
            <option>PM</option>
          </FormControl>
        </FormGroup>
      </Form>
    );
    // return <h2>Welcome To Traveling Customer</h2>;
  }
}

DropdownTime.defaultProps = {
  spec: null,
};
export default DropdownTime;
