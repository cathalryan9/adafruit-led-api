var Nav = ReactBootstrap.Nav;
var NavItem = ReactBootstrap.NavItem;

class NavBar extends React.Component{

   render() {

      return (
        <div>
            <Nav bsStyle="pills" justified>
                <NavItem href="/"><strong>LED-Interface</strong></NavItem>
                <NavItem href="/">Home</NavItem>
                <NavItem href="/file">Files</NavItem>
                <NavItem href="/">Upload</NavItem>
                <NavItem href="/parameter">Settings</NavItem>
                <NavItem disabled></NavItem>
                <NavItem href="/">LogIn</NavItem>
            </Nav>
        </div>
      );
   }
}

export default NavBar;