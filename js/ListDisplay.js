import React, { Component } from 'react';
import CommunicationButton from './CommunicationButton';

class ListDisplay extends Component {
  constructor(props) {
    super(props);
    this.state = {
      items: [],
      // items: this.props.items,
    };
    this.updateList = this.updateList.bind(this);
  }
  updateList(newItem) {
    console.log('updateList');
    // this.state.items[newItem.name] = newItem.id;
    this.setState({ items: this.state.items.concat([newItem]) });
    this.props.map.updateLocationList(newItem);
  }
  render() {
    const list = this.state.items;
    const currentLocation = this.props.map.state.center;
    const info = { places: list, start_loc: currentLocation };
    return (
      <div>
        <h1>Fork this List Display</h1>
        <ul>
          { list.map(item => <li key={item.id}>{item.name}</li>)}
        </ul>
        <CommunicationButton sendInfo={info} text="Done" />
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
