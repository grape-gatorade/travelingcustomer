/* eslint-env browser */
import React, { Component } from 'react';
import Button from 'react-bootstrap/lib/Button';


// This class is responsible for sending the data entered by the user to the
// flask server via a POST request, and receiving the response of that
// request from the server.
class CommunicationButton extends Component {
  constructor(props) {
    super(props);
    this.state = {
      text: this.props.text,
    };
    this.sendFetchRequest = this.sendFetchRequest.bind(this);
  }

  // Response of the POST Request calls this.props.onReceive
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
          className="btn btn-success"
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
