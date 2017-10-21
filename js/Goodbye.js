import React from 'react';
import ReactDOM from 'react-dom'
import {ScriptCache} from 'google-maps-react/dist/lib/ScriptCache'
import GoogleApi from 'google-maps-react/dist/lib/GoogleApi'
import GoogleApiComponent from 'google-maps-react/dist/';
import {Map, InfoWindow, Marker, GoogleApiWrapper} from 'google-maps-react';

class Goodbye extends React.Component {
  constructor(props) {
    super(props);
    //const {lat, lng} = this.props.initialCenter;
    this.state = {
      date: new Date()
    };
  }
  render() {
    return (

      <div>
      <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
      <div> Goodbye, World, {this.props.name}</div>

        <Map google={this.props.google} zoom={10} initialCenter={{
            lat: 40.854885,
            lng: -88.081807
          }}>

          <Marker onClick={this.onMarkerClick}
                  name={'Current location'} />


        </Map>
      </div>
    );
  }

}

//componentDidMount()

export default GoogleApiWrapper({
  apiKey: ('AIzaSyAZyEGbbz1wMFvjbX0yS_LDCG0WOyouWjk')
}) (Goodbye);
