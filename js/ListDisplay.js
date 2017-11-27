import React, { Component } from 'react';
import ListItem from './ListItem';
import styles from '../CSS/Thumbnail.css';

/*
Requiresd props: items =  list of items

Displays list of items as ListItem objects
*/
class ListDisplay extends Component {
  render() {
    console.log('render list display props: ', this.props);
    const list = this.props.items;
    return (
      <div style={styles.list}>
        <ul>
          { list.map(item => (
            <div key={item.id}>
              <ListItem key={item.id} name={item.name} />
            </div>
          ))}
        </ul>
      </div>);
  }
}
ListDisplay.defaultProps = {
  items: [],
};
export default ListDisplay;
