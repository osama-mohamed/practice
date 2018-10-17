const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");
const ejs = require("ejs");
const Nexmo = require("nexmo");
const port = process.env.PORT || 3000;
const app = express();
const socketio = require("socket.io");

app.set("views", path.join(__dirname, "views"));
app.set("view engine", "html");
app.engine("html", ejs.renderFile);
app.use(express.static(path.join(__dirname, "public")));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
require("dotenv").config();

const nexmo = new Nexmo(
  {
    apiKey: process.env.APIKEY,
    apiSecret: process.env.APISECRET
  },
  { debug: true }
);

app.get("/", (req, res) => {
  res.render("index");
});

app.post("/", (req, res) => {
  const number = req.body.number;
  const text = req.body.text;
  nexmo.message.sendSms(
    "OSAMA MOHAMED",
    number,
    text,
    { type: "unicode" },
    (err, responseData) => {
      if (err) {
        console.log(err);
      } else {
        const data = {
            id: responseData.messages[0]['message-id'],
            number: responseData.messages[0]['to']
        };
        io.emit('smsStatus', data);
      }
    }
  );
});

const server = app.listen(port, () => {
  console.log("Server started on port " + port);
});


const io = socketio(server);
io.on('connection', (socket) => {
    console.log('Connected');
    io.on('disconnect', () => {
        console.log('Disconnected');
    });
});