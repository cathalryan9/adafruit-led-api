import RunText from './RunText';
import React from 'react';
import { GithubPicker } from 'react-color';
var Button = ReactBootstrap.Button;
var Grid = ReactBootstrap.Grid;
var Row = ReactBootstrap.Row;
var Col = ReactBootstrap.Col;
var DropdownButton = ReactBootstrap.DropdownButton;
var DropdownMenu = ReactBootstrap.Dropdown.Menu;
var MenuItem = ReactBootstrap.MenuItem;

class File extends React.Component {

constructor() {
    super();
    this.handleChange = this.handleChange.bind(this);
    this.changeSelectedFile= this.changeSelectedFile.bind(this);

    /*this.data={input_data};*/
    this.state = {
      color: {
      r: '184',
      g: '0',
      b: '0',
      a: '1',
      },
      files: [],
      dropdownValue: 'Select a file',

    };
    this.colours = ['#B80000', '#DB3E00', '#FCCB00', '#008B02', '#1273DE', '#004DCF', '#5300EB', '#EB9694', '#FAD0C3', '#FEF3BD', '#FFFFFF', '#BEDADC', '#C4DEF6'];

}

changeSelectedFile(e){
    this.setState({dropdownValue: e}) ;
}

componentWillMount(){
    var data = this.props.data.input_data;
    for(var i in data.files)
            this.state.files.push(data.files[i].name + data.files[i].type);

}

httpPostToAPI(e, mode){
        var url = "http://127.0.0.1:5000/run";
        var method = "POST";
        console.log(mode);
        if (mode == 'clock'){
            var postData = '{"file": "' + mode + '", "duration": 10 }';
        }
        else if(mode=='file') {
            var postData = '{"file": "' + this.state.dropdownValue + '", "duration": 10 }';
        }
        else if(mode=='countdown') {
            var postData = '{"file": "' + mode + '", "duration": 10 }';
        }

        var async = true;
        var request = new XMLHttpRequest();
        request.onload = function () {
           var status = request.status; // HTTP response status, e.g., 200 for "200 OK"
           var data = request.responseText; // Returned data, e.g., an HTML document.
        }

        request.open(method, url, async);
        request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

        console.log(postData);
        request.send(postData);
       };

handleChange(color){
  this.setState({ color: color.rgb });
  console.log(this.state.color);
};

       render() {

          return (
          <div>
             <Grid>
                <Row className="show-grid">
                  <Col className="fileColumn" xs={6} md={4}>
                    <DropdownButton title={this.state.dropdownValue} onSelect={(e) => this.changeSelectedFile(e)} id="bg-nested-dropdown">
                    {this.state.files.map(file => <MenuItem eventKey={file} key={file}>{file.replace(/^.*[\\\/]/, '')}</MenuItem>)}
                    </DropdownButton
                  </ Col>
                  <Col className="fileColumn" xs={6} md={4}>
                     <Button bsStyle="primary" bsSize="large" block onClick={(e) => this.httpPostToAPI(e, 'file')}>Play File</Button>
                  </ Col>
                  <Col className="fileColumn" xs={6} md={4}>
                     <Button bsStyle="primary" bsSize="large" block onClick={(e) => this.httpPostToAPI(e, 'clock')}>Clock</Button>
                  </ Col>
                </Row>
                <Row className="show-grid">
                  <RunText color={this.state.color} />
                  <Col className="fileColumn" xs={6} md={4}>
                    <GithubPicker triangle = 'hide' width='350px' colors={this.colours} color={ this.state.color } onChange={ this.handleChange } />
                  </ Col>
                </Row>
                <Row className="show-grid">
                  <Col className="fileColumn" xs={6} md={4}>
                  <Button bsStyle="primary" bsSize="large" block onClick={(e) => this.httpPostToAPI(e, 'countdown')}>Countdown</Button>
                  </ Col>
                </Row>
             </Grid>
             </div>
          );
       }
}
export default File;