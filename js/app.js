/* eslint-env browser */
import React from 'react';
import ReactDOM from 'react-dom';
import Hello from './Hello';
import Map from './Map';
import SearchBar from './SearchBar';

let map = null;
const API_KEY = 'AIzaSyDA3tCPe5-nZ7i8swYDskytH2cmQq6lBiA';

const assignCurrentLocation = function assignCurrentLocation(position) {
  const currentLocation = { lat: position.coords.latitude, lng: position.coords.longitude };
  if (map !== null) {
    map.updateCenter(currentLocation);
  }
};

if (typeof window !== 'undefined') {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(assignCurrentLocation);
  }
  map = ReactDOM.render(<Map key={API_KEY} />, window.document.getElementById('reactMap'));
  ReactDOM.render(<Hello />, window.document.getElementById('helloWorld'));
  ReactDOM.render(<SearchBar map={map} />, window.document.getElementById('searchBar'));
}
