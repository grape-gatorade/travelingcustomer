import React, { Component } from 'react';
import PropTypes from 'prop-types';
import shouldPureComponentUpdate from 'react-pure-render/function';

import { markerStyle, markerStyleHover } from './marker_style_with_hover';


// Component responsible for displaying a marker with the
// correct styling in the correct location
class Marker extends Component {
  static propTypes = {
    // use hover from controllable
    hover: PropTypes.bool,
    text: PropTypes.string,
    number: PropTypes.string,
  };

  static defaultProps = {
    hover: null,
    text: '',
    number: '0',
  }

  static defaultProps = {};
  shouldComponentUpdate = shouldPureComponentUpdate;

  render() {
    const style = this.props.hover ? markerStyle : markerStyleHover;

    return (
      <div className="hint--html hint--top" style={style}>
        <div>{this.props.number}</div>
        <div className="hint__content">
          {this.props.text}
        </div>
      </div>
    );
  }
}
export default Marker;
