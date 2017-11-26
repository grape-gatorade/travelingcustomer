import React from 'react';
import PlacesAutocomplete, { geocodeByAddress, getLatLng } from 'react-places-autocomplete';
import { Form } from 'react-bootstrap';
import styles from '../CSS/Thumbnail.css';

/*
Require props: function onUpdate
Search Bar that finds nearby locations and sends them to parent list
*/
class SearchBar extends React.Component {
  constructor(props) {
    super(props);
    this.state = { address: '' };
    this.onChange = this.onChange.bind(this);
    this.handleSelect = this.handleSelect.bind(this);
  }

  // updates the address state variable
  onChange(address) {
    this.setState({ address });
  }

  handleSelect(address, placeId) {
    console.log('handle select called');
    geocodeByAddress(address).then(results => getLatLng(results[0]))
      .then((latLng) => {
        console.log('Success', latLng);
        const x = { name: address, id: placeId, latLng };
        if (this.props.onUpdate != null) {
          console.log('We can update the container');
          this.props.onUpdate(x);
        }
      })
      .catch(error => console.error('Error', error));
    // clearing the address field
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
      <Form>
        <PlacesAutocomplete
          inputProps={inputProps}
          options={options}
          onSelect={this.handleSelect}
          styles={styles.searchBar}
        />
      </Form>
    );
  }
}

export default SearchBar;
