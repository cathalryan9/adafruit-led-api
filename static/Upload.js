class Upload extends React.Component {

       render() {
       var readFiles = function(e) {
          var url = "http://127.0.0.1:5000/file";
        var method = "POST";
        var file = document.getElementById("file-content").files;
        console.log(file);
        var postData = {file};


        var async = true;

        var request = new XMLHttpRequest();

        request.onload = function () {
           var status = request.status; // HTTP response status, e.g., 200 for "200 OK"
           var data = request.responseText; // Returned data, e.g., an HTML document.
        }

        request.open(method, url, async);

        request.setRequestHeader("Content-Type", "multipart/form-data");
        // Or... request.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");
        // Or... whatever

        // Actually sends the request to the server.
        console.log('Goes through the function')
        var formData = new FormData();
        formData.append("file", file);


        request.send(formData);
        //request.send(file);
          }



          return (
             <div>
            <form action = "http://127.0.0.1:5000/file" encType = 'multipart/form-data'
method = "POST" >
         <input type = "file" name = "file" />
         <input type = "submit"/>
      </form>

             </div>
          );
       }
}
