/* eslint-env browser */
import React from 'react';
import ReactDOM from 'react-dom';
import Hello from './Hello';
import Goodbye from './Goodbye';
import Demo from './Demo';

let currentLocation = {};

const assignCurrentLocation = function assignCurrentLocation(position) {
  currentLocation = { lat: position.coords.latitude, lng: position.coords.longitude };
  ReactDOM.render(<Goodbye center={currentLocation} />, window.document.getElementById('reactEntry2'));
};

if (typeof window !== 'undefined') {
  ReactDOM.render(<Hello />, window.document.getElementById('reactEntry'));
  ReactDOM.render(<Demo />, window.document.getElementById('reactMap'));
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(assignCurrentLocation);
  } else {
    ReactDOM.render(<Goodbye />, window.document.getElementById('reactEntry2'));
  }
}
