import React from 'react';
import ShowRoutesSelector from './ShowRoutes';
/*
Required props: foundpaths
list of path objects
Contains a radiobutton that always different routes to be displayed
*/
class DisplayRoutes extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedpath: null,
    };
  }

  render() {
    const foundPaths = this.props.foundpaths;
    const routes = this.props.paths;

    /* Conditional on whether paths were found or not */
    let fp = null;
    if (foundPaths) {
      fp = <ShowRoutesSelector routes={routes} />;
    } else {
      fp = (<div> No paths yet. Type in your desired locations
              in the search bar and press done.
            </div>);
    }
    return (
      <div>
        {fp}
      </div>
    );
  }
}
// contains the radio buttons
DisplayRoutes.defaultProps = {
  foundpaths: false,
  paths: null,
};
export default DisplayRoutes;
