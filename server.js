var http = require("http");
var app = require("./app");
var port = 8000;

http.createServer(app.handleRequest).listen(port, () => {
  console.log("Server started on port " + port);
});
