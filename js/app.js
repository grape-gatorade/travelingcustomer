import Hello from './Hello';
import Goodbye from './Goodbye'
//import MapContainer from './MapContainer';
import Demo from './Demo'
import React from 'react';
import ReactDOM from 'react-dom';

ReactDOM.render(<Hello/>, document.getElementById('reactEntry'));

ReactDOM.render(<Demo/>, document.getElementById('reactMap'));
ReactDOM.render(<Goodbye/>, document.getElementById('reactEntry2'));
