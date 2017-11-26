// /* eslint-env browser */
import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';
import Marker from './Marker';

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
    console.log('updateLocation ', newLocation);
    // this.setState({ locationsList: this.state.items.concat([newLocation]) });
    this.setState({ locationList: this.state.locationList.concat([newLocation]) });
  }

  changeLocationList(newList) {
    this.setState({ locationList: newList });
  }

  render() {
    const markers = this.state.locationList;
    console.log('Called');
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
            number="1"
          />
          {
            markers.map((marker, index) => (
              <Marker
                key={marker.id}
                lat={marker.latLng.lat}
                lng={marker.latLng.lng}
                text={marker.name}
                number={(index + 2).toString()}
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
  zoom: 12,
  style: { width: '50%', height: '50%', position: 'relative' },
  APIkey: 'AIzaSyDA3tCPe5-nZ7i8swYDskytH2cmQq6lBiA',
  locationList: [],
};

export default Map;
