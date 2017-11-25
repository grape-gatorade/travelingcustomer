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
    this.setState({ items: info.optimal.path });
    this.props.map.changeLocationList(info.optimal.path.slice(1, info.optimal.path.length - 1));
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

    return (
      <div>
        <h1>Locations:</h1>
        <ul>
          { list.map(item => <li key={item.id}>{item.name}</li>)}
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
