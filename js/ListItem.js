import React, { Component } from 'react';
import styles from '../CSS/Thumbnail.css';
// Expects the prop name
// Displays the items in a list with a delete button

class ListItem extends Component {
  render() {
    return <div style={this.props.style}>{this.props.name}</div>;
  }
}
ListItem.defaultProps = {
  name: '',
  style: styles.listitem,
};
export default ListItem;
