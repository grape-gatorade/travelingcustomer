/* eslint-env browser */
import React from 'react';
import ReactDOM from 'react-dom';
import Hello from './Hello';
import Goodbye from './Goodbye';
import Demo from './Demo';

if (typeof window !== 'undefined') {
  ReactDOM.render(<Hello />, window.document.getElementById('reactEntry'));
  ReactDOM.render(<Demo />, window.document.getElementById('reactMap'));
  ReactDOM.render(<Goodbye />, window.document.getElementById('reactEntry2'));
}
