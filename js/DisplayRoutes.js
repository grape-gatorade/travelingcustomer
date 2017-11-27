import React from 'react';
import { ButtonToolbar, ButtonGroup, Button, Form } from 'react-bootstrap';
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

    let button = null;
    if (isLoggedIn) {
      button = <LogoutButton onClick={this.handleLogoutClick} />;
    } else {
      button = <LoginButton onClick={this.handleLoginClick} />;
    }
    return (
      <div>
        <Greeting isLoggedIn={foundPaths} />
      </div>
    );
  }
}

// contains the radio buttons
function ShowRoutes(props) {
  return (
    <div>
      <div>Routes Found</div>
      <ButtonToolbar>
        <ButtonGroup justified type="checkbox">
          <Button href="#">Optimal Path</Button>
          <Button href="#">Closing Time Path</Button>
          <Button href="#">Distance Path</Button>
          <Button href="#">Default Path</Button>
        </ButtonGroup>
      </ButtonToolbar>
    </div>

  );
}

function GuestGreeting(props) {
  return (<div>To get started enter in your desired destinations in the search bar</div>);
}

function Greeting(props) {
  const isLoggedIn = props.isLoggedIn;
  if (isLoggedIn) {
    return <ShowRoutes />;
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
