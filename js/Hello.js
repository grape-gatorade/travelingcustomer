import React, { Component } from 'react';
import { Jumbotron, Button } from 'react-bootstrap';
import styles from '../CSS/Thumbnail.css';

class Hello extends Component {
  render() {
    const line = 'Let\'s find your optimal path';
    return (
      <Jumbotron style={styles.welcome}>
        <h1>Welcome To Traveling Customer</h1>
        <p>{line}</p>
        <p><Button bsStyle="primary">Learn more</Button></p>
      </Jumbotron>);
    // return <h2>Welcome To Traveling Customer</h2>;
  }
}

export default Hello;
