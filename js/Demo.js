import React from 'react';
import { geolocated, geoPropTypes } from 'react-geolocated';


class Demo extends React.Component {
  render() {
    if (!this.props.isGeolocationAvailable) {
      return <div>Your browser does not support Geolocation</div>;
    } else if (!this.props.isGeolocationEnabled) {
      return <div>Geolocation is not enabled</div>;
    } else if (this.props.coords) {
      return (
        <div>
          <table>
            <tbody>
              <tr><td>latitude</td><td>{this.props.coords.latitude}</td></tr>
              <tr><td>longitude</td><td>{this.props.coords.longitude}</td></tr>
              <tr><td>altitude</td><td>{this.props.coords.altitude}</td></tr>
              <tr><td>heading</td><td>{this.props.coords.heading}</td></tr>
              <tr><td>latitude</td><td>{this.props.coords.latitude}</td></tr>
            </tbody>
          </table>
        </div>);
    }

    return <div>Getting the location data&hellip; </div>;
  }
}

// Using Object.assign
Demo.propTypes = Object.assign({}, Demo.propTypes, geoPropTypes);
// Using ES6 object spread syntax
// Demo.propTypes = {...Demo.propTypes, ...geoPropTypes};

export default geolocated()(Demo);