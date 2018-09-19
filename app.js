var http = require("http");
var module1 = require("./module1");
var module2 = require("./module2");
var port = 8000;

function onRequest(request, response) {
  response.writeHead(200, { "Content-Type": "text/plain" });
  response.write(module1.myString);
  response.write(module2.myVar);
  module1.myFunction();
  module2.myFunc();
  response.end();
}
http.createServer(onRequest).listen(port, () => {
  console.log("Server started on port " + port);
});
