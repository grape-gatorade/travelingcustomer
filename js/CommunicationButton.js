/* eslint-env browser */
import React, { Component } from 'react';

const sendFetchRequest = function sendFetchRequest(data) {
  fetch('http://127.0.0.1:5000/', {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  }).then((response) => {
    response.json().then((jsonData) => {
      console.log(jsonData);
    });
  });
};

class CommunicationButton extends Component {
  render() {
    return (
      <button
        type="submit"
        onClick={() => {
          const sendData = { info: this.props.sendInfo };
          sendFetchRequest(sendData);
        }}
      >Talk to Server
      </button>);
  }
}

export default CommunicationButton;
