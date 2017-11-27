import React from 'react';
import { ButtonToolbar, ToggleButtonGroup, ToggleButton } from 'react-bootstrap';
import ListDisplay from './ListDisplay';
// import Hello from './Hello';
import ShowRoutesSelector from './ShowRoutes';
/*
Required props: foundpaths
*/
class DisplayRoutes extends React.Component {
  constructor(props) {
    super(props);
    this.state = { isLoggedIn: false };
  }

  render() {
    const foundPaths = this.props.foundpaths;
    const routes = this.props.paths;

    let fp = null;
    if (foundPaths) {
      // fp = <div> found path true</div>;
      fp = <ShowRoutesSelector routes={routes} />;
    } else {
      fp = <div> No paths yet</div>;
      // fp = <ShowRoutesSelector routes="put routes here" />;
      // <Greeting found={foundPaths} paths={routes} />
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
