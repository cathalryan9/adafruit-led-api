var Button = ReactBootstrap.Button;
class RunText extends React.Component {

httpPostToAPI(e){
        var url = "http://127.0.0.1:5000/runtext";
        var method = "POST";
        var postData = '{"text": "' + document.getElementById("text_input").value + '", "colour": "red", "font": "7x13.bdf" }';
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

          return (
             <div>
             <input id='text_input'></input>
             <Button bsStyle="primary" bsSize="large" block onClick={(e) => this.httpPostToAPI()}>Text</Button>
             </div>
          );
       }
}

export default RunText;