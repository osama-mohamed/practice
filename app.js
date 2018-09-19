var http = require("http");
var fs = require("fs");
var port = 8000;

function onRequest(request, response) {
  response.writeHead(200, { "Content-Type": "text/html" });
  fs.readFile("./index.html", null, function(error, data) {
    if (error) {
      response.writeHead(404);
      response.write("file not found!");
    } else {
      response.write(data);
    }
    response.end();
  });
}

http.createServer(onRequest).listen(port, () => {
  console.log("Server started on port " + port);
});
