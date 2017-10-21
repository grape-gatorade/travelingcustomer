import Hello from './Hello';
import Goodbye from './Goodbye'
//import MapContainer from './MapContainer';
//import Container from './Container'
import React from 'react';
import ReactDOM from 'react-dom';

ReactDOM.render(<Hello/>, document.getElementById('reactEntry'));
ReactDOM.render(<Goodbye/>, document.getElementById('reactEntry2'));
//ReactDOM.render(<Container/>, document.getElementById('reactMap'));
