var Button = ReactBootstrap.Button;
var Grid = ReactBootstrap.Grid;
var Row = ReactBootstrap.Row;
var Col = ReactBootstrap.Col;


class File extends React.Component {

httpPostToAPI(e, mode){
        var url = "http://127.0.0.1:5000/run";
        var method = "POST";
        console.log(mode);
        if (mode == 'clock'){
            var postData = '{"file": "' + mode + '", "duration": 10 }';

        }
        else if(mode=='file') {
            var file_name = document.getElementById("file_name_input").value;
            console.log(file_name);
            var postData = '{"file": "' + document.getElementById("file_name_input").value + '", "duration": 10 }';
        }

        var async = true;
        var request = new XMLHttpRequest();
        request.onload = function () {
           var status = request.status; // HTTP response status, e.g., 200 for "200 OK"
           var data = request.responseText; // Returned data, e.g., an HTML document.
        }

        request.open(method, url, async);
        request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

        console.log('Goes throught the function');
        console.log(postData);

        request.send(postData);
       }

       render() {

          return (
             <div>
             <div>{{ input_data }}</div>
             <input id='file_name_input'></input>
             <Grid>
                <Row className="show-grid">
                  <Col xs={6} md={4}>
                     <Button bsStyle="primary" bsSize="large" block onClick={(e) => this.httpPostToAPI(e, 'file')}>Play File</Button>
                  </ Col>
                  <Col xs={6} md={4}>
                     <Button bsStyle="primary" bsSize="large" block onClick={(e) => this.httpPostToAPI(e, 'clock')}>Clock</Button>
                  </ Col>
                </Row>
             </Grid>
             <Upload />
             </div>
          );
       }
}