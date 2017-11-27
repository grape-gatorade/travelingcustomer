import React, { Component } from 'react';
import { ButtonToolbar, ToggleButtonGroup, ToggleButton } from 'react-bootstrap';
import ListDisplay from './ListDisplay'

class ShowRoutesSelector extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selected: 0,
    };
    this.onChange = this.onChange.bind(this);
  }
  onChange(value) {
    console.log('Display OnChange called', value);
    // selected = props.paths[value].path;
    // console.log('selected ', selected);
    this.setState({ selected: value });
  }
  render() {
    const s = this.state.selected;
    console.log("ShowRoutesSelector is rendering", this.props.routes[s].path);

    const selectedRoute = this.props.routes[s].path;
    const list = <ListDisplay items={selectedRoute} />;
    return (
      <div>
        <div> Shouw route </div>
        {list}
        <ButtonToolbar>
          <ToggleButtonGroup type="radio" name="options" onChange={this.onChange} defaultValue={0}>
            <ToggleButton value={0} >Optimal Path</ToggleButton>
            <ToggleButton value={1} >Closing Time Path</ToggleButton>
            <ToggleButton value={2} >Distance Path</ToggleButton>
            <ToggleButton value={3} >Default Path</ToggleButton>
          </ToggleButtonGroup>
        </ButtonToolbar>
      </div>
    );
  }
}
ShowRoutesSelector.defaultProps = {
  routes: null,
};
export default ShowRoutesSelector;
