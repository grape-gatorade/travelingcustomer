import React, { Component } from 'react';
import CommunicationButton from './CommunicationButton';
import ListItem from './ListItem';
import styles from '../CSS/Thumbnail.css';

class ListDisplay extends Component {
  constructor(props) {
    super(props);
    this.state = {
      items: [],
      // items: this.props.items,
    };
    this.updateList = this.updateList.bind(this);
    this.handleRecieveInfo = this.handleRecieveInfo.bind(this);
  }
  updateList(newItem) {
    console.log('updateList');
    // this.state.items[newItem.name] = newItem.id;
    this.setState({ items: this.state.items.concat([newItem]) });
    this.props.map.updateLocationList(newItem);
  }
  handleRecieveInfo(info) {
    console.log('handleRecieveInfo', info.path);
    this.setState({ items: info.path });
  }
  render() {
    const list = this.state.items;
    const currentLocation = this.props.map.state.center;
    const info = { places: list, start_loc: currentLocation };
    const comButton =
      (<CommunicationButton
        sendInfo={info}
        onRecieve={this.handleRecieveInfo}
        text="Done"
      />);
    // Dead code: <li key={item.id}>{item.name}</li>
    return (
      <div style={styles.list}>
        <h1>Locations:</h1>
        <ul>
          { list.map(item => (
            <div key={item.id}>
              <ListItem key={item.id} name={item.name} />
            </div>
          ))}
        </ul>
        {comButton}
      </div>);
  }
}
ListDisplay.defaultProps = {
  items: [],

};
export default ListDisplay;
// const places = {props.items.map((item =>
//   <div key={item.name}>
//     <h3>{item.name}</h3>
//     <p>{item.id}</p>
//   </div>
// )};
