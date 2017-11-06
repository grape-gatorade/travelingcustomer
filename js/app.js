/* eslint-env browser */
import React from 'react';
import ReactDOM from 'react-dom';
import GoogleMapsShareButton from './GoogleMapsShareButton';
import Hello from './Hello';
import Map from './Map';
import SearchBar from './SearchBar';
import ListDisplay from './ListDisplay';


const API_KEY = 'AIzaSyBuGbc491h07Hp-ao-6o-dkLmUUX9OG_ho';

const assignCurrentLocation = function assignCurrentLocation(position, mapToAssign) {
  const currentLocation = { lat: position.coords.latitude, lng: position.coords.longitude };
  if (mapToAssign !== null) {
    mapToAssign.updateCenter(currentLocation);
  }
};
if (typeof window !== 'undefined') {
  const map = ReactDOM.render(<Map APIkey={API_KEY} />, window.document.getElementById('reactMap'));
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition((position) => {
      assignCurrentLocation(position, map);
    });
  }
  ReactDOM.render(<Hello />, window.document.getElementById('helloWorld'));
  const locationsList = ReactDOM.render(<ListDisplay map={map} />, window.document.getElementById('locations_list'));
  ReactDOM.render(<SearchBar map={map} loclist={locationsList} />, window.document.getElementById('searchBar'));
  ReactDOM.render(<GoogleMapsShareButton text="Send Path To Google Maps" list={locationsList} />, window.document.getElementById('sendToServerButton'));
}
