import React, { Component } from 'react';
import { Jumbotron, Button } from 'react-bootstrap';
import styles from '../CSS/Thumbnail.css';

class Hello extends Component {
  render() {
    return (
      <Jumbotron style={styles.welcome}>
        <h1>Welcome To Traveling Customer</h1>
        <p>Lets find your optimal path</p>
        <p><Button bsStyle="primary">Learn more</Button></p>
      </Jumbotron>);
    // return <h2>Welcome To Traveling Customer</h2>;
  }
}

export default Hello;
