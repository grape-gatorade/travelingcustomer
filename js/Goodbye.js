/* eslint-env browser */
import React from 'react';
import PropTypes from 'prop-types';
// import {ScriptCache} from 'google-maps-react/dist/lib/ScriptCache';
// import GoogleApi from 'google-maps-react/dist/lib/GoogleApi';
// import GoogleApiComponent from 'google-maps-react/dist/';
import { Map, Marker, GoogleApiWrapper } from 'google-maps-react';

class Goodbye extends React.Component {
  constructor(props) {
    super(props);
    // geo = navigator.geolocation;
    console.log('Constr');
    // const {lat, lng} = this.props.initialCenter;
    this.state = {
      date: new Date(),
      centerAroundCurrentLocation: true,
    };
  }

  componentDidMount() {
    console.log('Component DID MOUNT!');
  }
  render() {
    return (
      <div>
        <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
        <div> Goodbye, World, {this.props.name}</div>
        <div>
          <Map
            google={this.props.google}
            zoom={10}
            initialCenter={{
            lat: 40.854885,
            lng: -88.081807,
            }}
            style={{ width: '50%', height: '50%', position: 'relative' }}
            centerAroundCurrentLocation={this.state.centerAroundCurrentLocation}
          >
            <Marker
              onClick={this.onMarkerClick}
              name="Current location"
            />
          </Map>
        </div>
      </div>
    );
  }
}

Goodbye.defaultProps = {
  name: 'My Name',
  google: {
    name: 'google',
  },
};

Goodbye.propTypes = {
  name: PropTypes.string,
  google: PropTypes.object,
};

const options = {
  enableHighAccuracy: true,
  timeout: 5000,
  maximumAge: 0,
};

function success(pos) {
  const crd = pos.coords;

  console.log('Your current position is:');
  console.log(`Latitude : ${crd.latitude}`);
  console.log(`Longitude: ${crd.longitude}`);
  console.log(`More or less ${crd.accuracy} meters.`);
}

function error(err) {
  console.warn(`ERROR(${err.code}): ${err.message}`);
}

if (typeof window !== 'undefined') {
  window.navigator.geolocation.getCurrentPosition(success, error, options);
}
// componentDidMount()

export default GoogleApiWrapper({
  apiKey: ('AIzaSyAZyEGbbz1wMFvjbX0yS_LDCG0WOyouWjk'),
})(Goodbye);
