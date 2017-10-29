import React from 'react';
import PlacesAutocomplete, { geocodeByAddress, getLatLng } from 'react-places-autocomplete';

class SearchBar extends React.Component {
  constructor(props) {
    super(props);
    this.state = { address: 'Troy, NY' };
    this.onChange = this.onChange.bind(this);
    this.handleSelect = this.handleSelect.bind(this);
    this.handleFormSubmit = this.handleFormSubmit.bind(this);
  }

  onChange(address) {
    this.setState({ address });
  }

  handleSelect(address, placeId) {
    const item = { name: address, id: placeId };
    console.log('handle select called');
    console.log(address);
    console.log(placeId);
    console.log(this.props.loclist.props.items);
    this.props.loclist.updateList(item);
    // this.setState({ address, placeId });
  }


  handleFormSubmit(event) {
    event.preventDefault();

    // Move to point on map.
    geocodeByAddress(this.state.address)
      .then(results => getLatLng(results[0]))
      .then(latLng => this.props.map.updateCenter(latLng))
      .catch();
  }

  render() {
    const inputProps = {
      value: this.state.address,
      onChange: this.onChange,
      placeholder: 'Search Places...',
    };


    const options = {
      googleLogo: true,
    };

    return (
      <form
        onSubmit={this.handleFormSubmit}
      >
        <PlacesAutocomplete
          inputProps={inputProps}
          options={options}
          onSelect={this.handleSelect}
        />
        <button type="submit">Submit</button>
      </form>
    );
  }
}

export default SearchBar;
