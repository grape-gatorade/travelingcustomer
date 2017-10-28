// /* eslint-env browser */
import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';

class Map extends Component {
  constructor(props) {
    super(props);
    this.state = {
      center: {
        lat: this.props.center.lat,
        lng: this.props.center.lng,
      },
    };
    this.updateCenter = this.updateCenter.bind(this);
  }

  updateCenter(newCenter) {
    this.setState({ center: newCenter }); 
  }


  render() {
    console.log(this.state.center);
    // console.log(this.props.center.lat);
    // console.log(this.props.center.lng);
    return (
      <GoogleMapReact
        center={this.state.center}
        defaultZoom={this.props.zoom}
        style={this.props.style}
        bootstrapURLKeys={{
          key: this.props.key,
        }}
      />
    );
  }
}

Map.defaultProps = {
  center: { lat: 59.95, lng: 30.33 },
  zoom: 11,
  style: { width: '50%', height: '50%', position: 'relative' },
  key: 'AIzaSyDA3tCPe5-nZ7i8swYDskytH2cmQq6lBiA',
};

export default Map;