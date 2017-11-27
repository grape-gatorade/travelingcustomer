/* eslint-env browser */
import React, { Component } from 'react';
import { Button } from 'react-bootstrap';

class GoogleMapsShareButton extends Component {
  static defaultProps = {
    text: 'Open Google Maps',
  }

  constructor(props) {
    super(props);

    this.openGoogleMapsWindow = this.openGoogleMapsWindow.bind(this);
  }

  openGoogleMapsWindow() {
    const url = 'https://www.google.com/maps/dir/';

    const listItems = this.props.items;

    const currentLocationString = `${listItems[0].latLng.lat},${listItems[0].latLng.lng}/`;

    console.log(currentLocationString);

    let waypointString = '';

    for (let i = 1; i < listItems.length - 1; i += 1) {
      waypointString += listItems[i].name.replace(' ', '+');
      waypointString += '/';
    }

    window.open(url + currentLocationString + waypointString + currentLocationString);
  }

  render() {
    return (
      <div>
        <Button onClick={this.openGoogleMapsWindow}>
          {this.props.text}
        </Button>
      </div>);
  }
}
export default GoogleMapsShareButton;
