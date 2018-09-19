var http = require("http");
var module1 = require("./module1");
var port = 8000;

function onRequest(request, response) {
  response.writeHead(200, { "Content-Type": "text/plain" });
  response.write(module1.myString);
  module1.myFunction();
  response.end();
}
http.createServer(onRequest).listen(port, () => {
  console.log("Server started on port " + port);
});
