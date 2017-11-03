import React, { Component } from 'react';

const AnyReactComponent = ({ text }) => (
  <div style={{
                position: 'relative',
                color: 'black',
                background: 'green',
                height: 5,
                width: 5,
              }}
  >
    {text}
  </div>
);
class Marker extends Component {
  render() {
    return (
      <AnyReactComponent
        text={this.props.text}
      />);
  }
}

export default Marker;
