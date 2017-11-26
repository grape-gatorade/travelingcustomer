/* eslint-env browser */
import React, { Component } from 'react';
import Button from 'react-bootstrap/lib/Button';
// import { Button } from 'react-bootstrap';


class CommunicationButton extends Component {
  constructor(props) {
    super(props);
    this.state = {
      text: this.props.text,
    };
    this.sendFetchRequest = this.sendFetchRequest.bind(this);
  }
  sendFetchRequest(data) {
    fetch('http://127.0.0.1:5000/', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    }).then((response) => {
      response.json().then((jsonData) => {
        console.log('send fetch', jsonData);
        this.props.onRecieve(jsonData);
      });
    });
  }


  render() {
    return (
      <div>
        <Button
          onClick={() => {
            const sendData = { info: this.props.sendInfo };
            this.sendFetchRequest(sendData);
          }}
        >{this.state.text}
        </Button>
      </div>);
  }
}

CommunicationButton.defaultProps = {
  text: 'Send to Server',
  sendInfo: 'Error',
};

export default CommunicationButton;
