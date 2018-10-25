const express = require("express");
const path = require("path");
const mongoose = require("mongoose");
const exphbs = require("express-handlebars");

const app = express();
const port = process.env.PORT || 3000;

mongoose.Promise = global.Promise;

mongoose
  .connect(
    "mongodb://localhost:27017/videoidea",
    { useNewUrlParser: true }
  )
  .then(() => {
    console.log("MongoDB connected ...");
  })
  .catch(err => console.log(err));

require("./models/Idea");
const Idea = mongoose.model("ideas");

app.set("views", path.join(__dirname, "views"));
app.engine(
  "handlebars",
  exphbs({
    defaultLayout: "main"
  })
);
app.set("view engine", "handlebars");

app.get("/", (req, res) => {
  const title = "Hello osama";
  res.render("index", {
    title: title
  });
});

app.get("/about", (req, res) => {
  res.render("about");
});

app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
