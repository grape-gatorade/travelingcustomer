import React, { Component } from 'react';
import SearchBar from './SearchBar';
import ListDisplay from './ListDisplay';
import DropdownTime from './dropdownTime';
import CommunicationButton from './CommunicationButton'

class UserInputContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {
      location_list: [],
      recieved: [],
    };
    this.updateList = this.updateList.bind(this);
    this.handleRecieveInfo = this.handleRecieveInfo.bind(this);
  }
  updateList(newItem) {
    // this.state.items[newItem.name] = newItem.id;
    this.setState({ location_list: this.state.location_list.concat([newItem]) });
    console.log('updateList Container', this.state.location_list.length);
    /* Update the maps list */
    this.props.map_show.updateLocationList(newItem);
    // this.props.map.updateLocationList(newItem);
  }
  handleRecieveInfo(info) {
    console.log('handleRecieveInfo', info.path);
    this.setState({ recieved: info.path });
  }
  render() {
    console.log('render userinput: ', this.props);
    const currentLocation = this.props.map_show.state.center;
    const list = this.state.location_list;
    const info = { places: list, start_loc: currentLocation };
    const comButton =
      (<CommunicationButton
        sendInfo={info}
        onRecieve={this.handleRecieveInfo}
        text="Done"
      />);
    return (
      <div>
        <SearchBar onUpdate={this.updateList} />
        <DropdownTime spec="Start Time" />
        <DropdownTime spec="End Time" />
        <ListDisplay items={list} />
        {comButton}
      </div>
    );
  }
}
UserInputContainer.defaultProps = { map_show: null, current_loc: null };
export default UserInputContainer;
