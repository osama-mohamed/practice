const express = require("express");
const path = require("path");
const mongoose = require("mongoose");

// connect to database
mongoose.connect(
  "mongodb://localhost/nodekb",
  { useNewUrlParser: true }
);
let db = mongoose.connection;

// check DB connection
db.once("open", () => {
  console.log("Connected to MongoDB");
});

// check for DB errors
db.on("error", err => {
  console.log(err);
});

// init app
const app = express();

// bring in Models
let Article = require("./models/article");

// load view engine
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "pug");

// home route
app.get("/", (req, res) => {
  Article.find({}, (err, articles) => {
    if (err) {
      console.log(err);
    } else {
      res.render("index", {
        title: "Articles",
        articles: articles
      });
    }
  });
});

// add new article route
app.get("/articles/add", (req, res) => {
  res.render("add_article", {
    title: "Add Article"
  });
});

// start server
app.listen(3000, () => {
  console.log("Server started on port 3000");
});
