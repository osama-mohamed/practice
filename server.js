const express = require("express");
const port = process.env.PORT || 3000;
const app = express();
const server = require("http").createServer(app);
const io = require("socket.io").listen(server);

let users = [];
let connections = [];

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/index.html");
});

server.listen(port, () => {
  console.log("Server started on port " + port);
});

io.sockets.on("connection", socket => {
  connections.push(socket);
  console.log("Connected : %s sockets connected.", connections.length);

  // disconnect
  socket.on("disconnect", data => {
    // if (!socket.username) return;
    users.splice(users.indexOf(socket.username), 1);
    updateUsernames();
    connections.splice(connections.indexOf(socket), 1);
    console.log("Disconnected : %s sockets connected.", connections.length);
  });

  // send message
  socket.on("send message", data => {
    // console.log("msg  server.js: ", data);
    io.sockets.emit("new message", { msg: data, user: socket.username });
  });

  // new user
  socket.on("new user", (data, callback) => {
    // console.log("new user server.js: ", data);
    callback(true);
    socket.username = data;
    users.push(socket.username);
    updateUsernames();
  });

  function updateUsernames() {
    io.sockets.emit("get users", users);
  }
});
