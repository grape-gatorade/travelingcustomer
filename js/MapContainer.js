import React from 'react'
import ReactDOM from 'react-dom'
import {ScriptCache} from 'google-maps-react/dist/lib/ScriptCache'
import GoogleApi from 'google-maps-react/dist/lib/GoogleApi'
import {Component} from "react";


import {Map, InfoWindow, Marker, GoogleApiWrapper} from 'google-maps-react';

// ...

export class MapContainer extends React.Component {
  render() {
      return (
        <Map google={this.props.google} zoom={14}>

          <Marker onClick={this.onMarkerClick}
                  name={'Current location'} />

          <InfoWindow onClose={this.onInfoWindowClose}>
              <div>
                <h1>{this.state.selectedPlace.name}</h1>
              </div>
          </InfoWindow>
        </Map>
      );
    }
}

export default GoogleApiWrapper({
  apiKey: ('AIzaSyAZyEGbbz1wMFvjbX0yS_LDCG0WOyouWjk')
})(MapContainer)
