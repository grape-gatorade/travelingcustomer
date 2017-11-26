/* eslint-env browser */
import 'html-hint/dist/html-hint.min.css';
import React from 'react';
import ReactDOM from 'react-dom';
import GoogleMapsShareButton from './GoogleMapsShareButton';
import Hello from './Hello';
import Map from './Map';
import SearchBar from './SearchBar';
import ListDisplay from './ListDisplay';
import DropdownTime from './dropdownTime';
import UserInputContainer from './UserInputContainer';

const API_KEY = 'AIzaSyBuGbc491h07Hp-ao-6o-dkLmUUX9OG_ho';

// updates the center of the map given to be the user's current location.
const assignCurrentLocation = function assignCurrentLocation(position, mapToAssign) {
  const currentLocation = { lat: position.coords.latitude, lng: position.coords.longitude };
  if (mapToAssign !== null) {
    mapToAssign.updateCenter(currentLocation);
  }
};

if (typeof window !== 'undefined') {
  // Make sure we are in a browser environment,
  // Then get the current location.
  const map = ReactDOM.render(<Map APIkey={API_KEY} />, window.document.getElementById('reactMap'));
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition((position) => {
      assignCurrentLocation(position, map);
    });
  }
  ReactDOM.render(<UserInputContainer map_show={map} />, window.document.getElementById('userInput'));
  ReactDOM.render(<Hello />, window.document.getElementById('helloWorld'));
}
