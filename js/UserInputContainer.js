/* eslint-env browser */
import React, { Component } from 'react';
import SearchBar from './SearchBar';
import ListDisplay from './ListDisplay';
import DropdownTime from './dropdownTime';
import CommunicationButton from './CommunicationButton';
import DisplayRoutes from './DisplayRoutes';

/*
Required prop: map object
Contains all of the components and acts as a platform for them to communicate
*/
class UserInputContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {
      location_list: [],
      recieved: [],
      start_time: null,
      end_time: null,
    };
    this.updateList = this.updateList.bind(this);
    this.updateTime = this.updateTime.bind(this);
    this.handleRecieveInfo = this.handleRecieveInfo.bind(this);
  }
  updateList(newItem) {
    // this.state.items[newItem.name] = newItem.id;
    if (this.state.location_list.length >= 20) {
      // alert("Hello! I am an alert box!");
      // TODO: find alert button
      console.log('No more than 20 locations permitted');
      return;
    }
    this.setState({ location_list: this.state.location_list.concat([newItem]) });
    console.log('updateList Container', this.state.location_list.length);
    /* Update the maps list */
    this.props.map_show.updateLocationList(newItem);
    // this.props.map.updateLocationList(newItem);
  }

  /* called when one of the time components is changed and updates the state */
  updateTime(id, time) {
    if (id === 'start') {
      this.setState({ start_time: time });
    } else {
      this.setState({ end_time: time });
    }
  }
  /* recieves information from server and updates component state */
  handleRecieveInfo(info) {
    console.log('handleRecieveInfo', info);
    this.setState({ recieved: info });
    if (!info.path_found) {
      window.alert('Unable to find path!');
    }
    if (info.closed_stores) {
      window.alert('There were closed stores on your route!');
    }
  }

  render() {
    console.log('render userinput: ', this.props);
    const currentLocation = this.props.map_show.state.center;
    const list = this.state.location_list;
    const starttime = this.state.start_time;
    const endtime = this.state.end_time;
    const pathsfound = this.state.recieved.path_found;
    const info = {
      places: list,
      start_loc: currentLocation,
      start_time: starttime,
      end_time: endtime,
    };
    const comButton =
      (<CommunicationButton
        sendInfo={info}
        onRecieve={this.handleRecieveInfo}
        text="Done"
      />);
    return (
      <div>
        <SearchBar onUpdate={this.updateList} />
        <DropdownTime onUpdate={this.updateTime} id="start" spec="Start Time" />
        <DropdownTime onUpdate={this.updateTime} id="end" spec="End Time" />
        <ListDisplay items={list} />
        {comButton}
        <DisplayRoutes foundpaths={pathsfound} paths={this.state.recieved.paths} />
      </div>
    );
  }
}
UserInputContainer.defaultProps = { map_show: null, current_loc: null };
export default UserInputContainer;
