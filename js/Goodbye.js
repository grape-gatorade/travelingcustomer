// /* eslint-env browser */
import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';

const AnyReactComponent = ({ text }) => <div>{text}</div>;

class Goodbye extends Component {
  render() {
    // console.log(this.props.center.lat);
    // console.log(this.props.center.lng);
    return (
      <GoogleMapReact
        defaultCenter={this.props.center}
        defaultZoom={this.props.zoom}
        style={this.props.style}
      >
        <AnyReactComponent
          lat={59.955413}
          lng={30.337844}
          text="Kreyser Avrora"
        />
      </GoogleMapReact>
    );
  }
}

Goodbye.defaultProps = {
  center: { lat: 59.95, lng: 30.33 },
  zoom: 11,
  style: { width: '50%', height: '50%', position: 'relative' },
};

export default Goodbye;
