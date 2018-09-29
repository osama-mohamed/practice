const path = require("path");
const express = require("express");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
const config = require("./config/database");

mongoose.connect(
  config.database,
  { useNewUrlParser: true }
);
let db = mongoose.connection;
db.once("open", () => {
  console.log("Connected to MongoDB");
});
db.on("error", err => {
  console.log(err);
});

const app = express();
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, "public")));

let todos = require("./routes/todo");
app.use("/", todos);

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log("Server started on port " + port);
});
