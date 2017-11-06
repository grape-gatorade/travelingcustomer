import React, { Component } from 'react';
import { Button } from 'react-bootstrap';

class GoogleMapsShareButton extends Component {
  constructor(props) {
    super(props);
    this.state = {
      text: this.props.text,
    };

    this.openGoogleMapsWindow = this.openGoogleMapsWindow.bind(this);
  }

  openGoogleMapsWindow() {
    let url = 'https://www.google.com/maps/dir/';
    window.open(url);
  }

  render() {
    return (
      <div>
        <Button onClick={this.openGoogleMapsWindow}>
          {this.state.text}
        </Button>
      </div>);
  }
}
export default GoogleMapsShareButton;