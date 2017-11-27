import React from 'react';
import { ButtonToolbar, ToggleButtonGroup, ToggleButton, Form } from 'react-bootstrap';
/*
Required props: foundpaths
*/
class DisplayRoutes extends React.Component {
  constructor(props) {
    super(props);
    this.handleLoginClick = this.handleLoginClick.bind(this);
    this.handleLogoutClick = this.handleLogoutClick.bind(this);
    this.state = { isLoggedIn: false };
  }

  handleLoginClick() {
    this.setState({ isLoggedIn: true });
  }

  handleLogoutClick() {
    this.setState({ isLoggedIn: false });
  }

  render() {
    const isLoggedIn = this.state.isLoggedIn;
    const foundPaths = this.props.foundpaths;
    const routes = this.props.paths;

    let button = null;
    if (isLoggedIn) {
      button = <LogoutButton onClick={this.handleLogoutClick} />;
    } else {
      button = <LoginButton onClick={this.handleLoginClick} />;
    }
    return (
      <div>
        <Greeting found={foundPaths} paths={routes} />
      </div>
    );
  }
}



// contains the radio buttons
function ShowRoutes(props) {
  function onChange(value) {
    console.log('Display OnChange called', value)
    console.log(props.paths[value])
  }
  return (
    <div>
      <div>Routes Found</div>
      <ButtonToolbar>
        <ToggleButtonGroup type="radio" name="options" onChange={onChange} defaultValue={0}>
          <ToggleButton value={0} >Optimal Path</ToggleButton>
          <ToggleButton value={1} >Closing Time Path</ToggleButton>
          <ToggleButton value={2} >Distance Path</ToggleButton>
          <ToggleButton value={3} >Default Path</ToggleButton>
        </ToggleButtonGroup>
      </ButtonToolbar>
    </div>

  );
}

function GuestGreeting(props) {
  return (<div>To get started enter in your desired destinations in the search bar</div>);
}

function Greeting(props) {
  // const found = props.found;
  if (props.found) {
    return <ShowRoutes paths={props.paths} />;
  }
  // return <ShowRoutes />;
  return <GuestGreeting />;
}

function LoginButton(props) {
  return (
    <button onClick={props.onClick}>
      Login
    </button>
  );
}

function LogoutButton(props) {
  return (
    <button onClick={props.onClick}>
      Logout
    </button>
  );
}
DisplayRoutes.defaultProps = {
  foundpaths: false,
  paths: null,
};
export default DisplayRoutes;
