import React, { Component } from 'react';

class ListDisplay extends Component {
  constructor(props) {
    super(props);
    this.state = {
      items: [{ name: 'P-chops', id: 'pchop id' }, { name: 'Walmard', id: 'wally id' }],
      // items: this.props.items,
    };
    this.updateList = this.updateList.bind(this);
  }
  updateList(newItem) {
    console.log('updateList');
    console.log(newItem.id);
    // this.state.items[newItem.name] = newItem.id;
    this.setState({ items: this.state.items.concat([newItem]) });
    console.log(this.state.items);
  }
  render() {
    const list = this.state.items;
    return (
      <div>
        <h1>Fork this List Display</h1>
        <ul>
          { list.map(item => <li key={item.id}>{item.name}</li>)}
        </ul>
      </div>);
  }
}
ListDisplay.defaultProps = {
  items: [{ name: 'P-chops', id: 'pchop id' }, { name: 'Walmard', id: 'wally id' }],

};
export default ListDisplay;
// const places = {props.items.map((item =>
//   <div key={item.name}>
//     <h3>{item.name}</h3>
//     <p>{item.id}</p>
//   </div>
// )};
