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
    // const item = { name: address, id: placeId };
    console.log('handle select called');
    // this.props.loclist.updateList(item);

    geocodeByAddress(address).then(results => getLatLng(results[0]))
      .then((latLng) => {
        console.log('Success', latLng);
        const x = { name: address, id: placeId, latLng };
        this.props.loclist.updateList(x);
      })
      .catch(error => console.error('Error', error));
    // console.log('latlng', latlng);
    // this.setState({ address, placeId });

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
