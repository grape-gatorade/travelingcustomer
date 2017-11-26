import React, { Component } from 'react';
import { FormGroup, FormControl, ControlLabel, Form } from 'react-bootstrap';

/*
Generate a list of numbers
Required props = id, spec, onUpdate functions
Three drop down lists that allow the user to select a time
*/
class DropdownTime extends Component {
  static populateList(Num) {
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
      hour: 0,
      minute: 0,
      meridiem: 'AM',
    };
    this.handleSelectHour = this.handleSelectHour.bind(this);
    this.handleSelectMinute = this.handleSelectMinute.bind(this);
    this.handleSelectMeridiem = this.handleSelectMeridiem.bind(this);
  }
  /* Updates the state hour variable
  Updates the parent  */
  handleSelectHour(event) {
    const time = this.state;
    // console.log('handleSelectHour', time.hour);
    time.hour = parseInt(event.target.value, 10);
    this.setState({ hour: parseInt(event.target.value, 10) });
    this.props.onUpdate(this.props.id, time);
  }
  /* Updates the state minute
  Updates the parent  */
  handleSelectMinute(event) {
    const time = this.state;
    time.minute = parseInt(event.target.value, 10);
    this.setState({ minute: parseInt(event.target.value, 10) });
    this.props.onUpdate(this.props.id, time);
  }
  /* Updates the state meridium
  Updates the parent */
  handleSelectMeridiem(event) {
    this.setState({ meridiem: event.target.value });
    const time = this.state;
    time.meridiem = event.target.value;
    this.props.onUpdate(this.props.id, time);
  }
  render() {
    const horas = this.constructor.populateList(12);
    const minutos = this.constructor.populateList(60);
    return (
      <div>
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
            <FormControl
              componentClass="select"
              placeholder="select"
              onChange={this.handleSelectMeridiem}
            >
              <option>AM</option>
              <option>PM</option>
            </FormControl>
          </FormGroup>
        </Form>
      </div>
    );
    // return <h2>Welcome To Traveling Customer</h2>;
  }
}

DropdownTime.defaultProps = {
  spec: null,
  id: null,
  onUpdate: null,
};
export default DropdownTime;
