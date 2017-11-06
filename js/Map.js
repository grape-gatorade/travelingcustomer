// /* eslint-env browser */
import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';
import Marker from './Marker';


const AnyReactComponent = ({ text }) => (
  <div style={{
                position: 'relative',
                color: 'white',
                background: 'red',
                height: 40,
                width: 60,
                top: -20,
                left: -30,
              }}
  >
    {text}
  </div>
);

class Map extends Component {
  constructor(props) {
    super(props);
    this.state = {
      center: {
        lat: this.props.center.lat,
        lng: this.props.center.lng,
      },
      locationList: [],
    };
    this.updateCenter = this.updateCenter.bind(this);
    this.updateLocationList = this.updateLocationList.bind(this);
  }

  updateCenter(newCenter) {
    console.log('updateCenter ', newCenter.lat, ' ', newCenter.lng);
    this.setState({ center: newCenter });
  }

  updateLocationList(newLocation) {
    console.log('updateLocation ');
    // this.setState({ locationsList: this.state.items.concat([newLocation]) });
    this.setState((prevState, props) => {
      return { locationList: prevState.locationList.concat([newLocation]) };
    });
  }

  render() {
    const markers = this.state.locationList;
    return (
      <div>
        <GoogleMapReact
          center={this.state.center}
          defaultZoom={this.props.zoom}
          style={this.props.style}
          bootstrapURLKeys={{
            key: this.props.APIkey,
          }}
        >
          <Marker
            lat={this.state.center.lat}
            lng={this.state.center.lng}
            text="current location"
          />
          {
            markers.map(marker => (
              <Marker
                lat={marker.latLng.lat}
                lng={marker.latLng.lng}
                text={marker.name}
              />
            ))
          }
        </GoogleMapReact>
      </div>
    );
  }
}

Map.defaultProps = {
  center: { lat: 59.95, lng: 30.33 },
  zoom: 11,
  style: { width: '50%', height: '50%', position: 'relative' },
  APIkey: 'AIzaSyDA3tCPe5-nZ7i8swYDskytH2cmQq6lBiA',
  locationList: [],
};

export default Map;
