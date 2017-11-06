import React from 'react';
import PlacesAutocomplete, { geocodeByAddress, getLatLng } from 'react-places-autocomplete';

class SearchBar extends React.Component {
  constructor(props) {
    super(props);
    this.state = { address: '' };
    this.onChange = this.onChange.bind(this);
    this.handleSelect = this.handleSelect.bind(this);
  }

  onChange(address) {
    this.setState({ address });
  }

  handleSelect(address, placeId) {
    console.log('handle select called');
    geocodeByAddress(address)
      .then(results => getLatLng(results[0]))
      .then((latLng) => {
        const item = {
          name: address,
          id: placeId,
          lat: latLng.lat,
          lng: latLng.lng,
        };
        this.props.loclist.updateList(item);
      });

    this.setState({ address: '' });
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
      <form>
        <PlacesAutocomplete
          inputProps={inputProps}
          options={options}
          onSelect={this.handleSelect}
        />
      </form>
    );
  }
}

export default SearchBar;
