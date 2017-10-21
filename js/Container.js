import React from 'react'
import ReactDOM from 'react-dom'
import {ScriptCache} from 'google-maps-react/dist/lib/ScriptCache'
import GoogleApi from 'google-maps-react/dist/lib/GoogleApi'
import GoogleApiComponent from 'google-maps-react/dist/';
import {Component} from "react";
export class Container extends React.Component {
  render() {
    if (!this.props.loaded) {
      return <div>Loading...</div>
    }
    return (
      <div>Map will go here</div>
    )
  }
}

export default GoogleApiComponent({
  apiKey: 'AIzaSyAZyEGbbz1wMFvjbX0yS_LDCG0WOyouWjk'
})(Container)
