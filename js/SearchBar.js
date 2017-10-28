import React from 'react';
import PlacesAutocomplete, { geocodeByAddress, getLatLng } from 'react-places-autocomplete';

class SearchBar extends React.Component {
  constructor(props) {
    super(props);
    this.state = { address: 'Troy, NY' };
    this.onChange = this.onChange.bind(this);
    this.handleFormSubmit = this.handleFormSubmit.bind(this);
  }

  onChange(address) {
    this.setState({ address });
  }

  handleFormSubmit(event) {
    event.preventDefault();

    // Move to point on map.
    geocodeByAddress(this.state.address)
      .then(results => getLatLng(results[0]))
      .then(latLng => this.props.map.updateCenter(latLng))
      .catch(error => console.error('Error', error));
  }

  render() {
    const inputProps = {
      value: this.state.address,
      onChange: this.onChange,
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
        />
        <button type="submit">Submit</button>
      </form>
    );
  }
}

export default SearchBar;
