var Button = ReactBootstrap.Button;
var Grid = ReactBootstrap.Grid;
var Row = ReactBootstrap.Row;
var Col = ReactBootstrap.Col;
class RunText extends React.Component {

httpPostToAPI(e){
        var url = "http://127.0.0.1:5000/runtext";
        var method = "POST";
        var colour = '{"red":'+ this.props.color.r+',"green":'+ this.props.color.g+',"blue":'+ this.props.color.b+'}'
        var postData = '{"text": "' + document.getElementById("text_input").value + '", "colour":'+ colour +', "font": "7x13.bdf" }';
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
       }

       render() {

              console.log(this.props.color.r);

          return (
             <div>
             <Grid>
                <Row className="show-grid">
                  <Col xs={6} md={4}>
                  <input id='text_input'></input>
                  </ Col>
                  <Col xs={6} md={4}>
<Button style={{background: `rgba(${ this.props.color.r }, ${ this.props.color.g }, ${ this.props.color.b }, ${ this.props.color.a })`}} bsSize="large" block onClick={(e) => this.httpPostToAPI()}>Text</Button>
                  </ Col>
                  <Col xs={6} md={4}>

                  </ Col>
                </Row>
             </Grid>


             </div>
          );
       }
}

export default RunText;