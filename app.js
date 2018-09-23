const express = require("express");
const bodyParser = require("body-parser");
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

// body parser middleware
// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }));
// parse application/json
app.use(bodyParser.json());

// set public folder
app.use(express.static(path.join(__dirname, "public")));

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

// get article detail
app.get("/article/:id", (req, res) => {
  Article.findById(req.params.id, (err, article) => {
    if (err) {
      console.log(err);
    } else {
      res.render("article", {
        article: article
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

// add new article submit route
app.post("/articles/add", (req, res) => {
  let article = new Article();
  article.title = req.body.title;
  article.author = req.body.author;
  article.body = req.body.body;
  article.save(err => {
    if (err) {
      console.log(err);
      return;
    } else {
      res.redirect("/");
    }
  });
});

// load edit article foarm
app.get("/article/edit/:id", (req, res) => {
  Article.findById(req.params.id, (err, article) => {
    if (err) {
      console.log(err);
    } else {
      res.render("edit_article", {
        title: "Edit Article",
        article: article
      });
    }
  });
});

// save edited article
app.post("/article/edit/:id", (req, res) => {
  let article = {};
  article.title = req.body.title;
  article.author = req.body.author;
  article.body = req.body.body;

  let query = {_id: req.params.id}
  Article.update(query, article, err => {
    if (err) {
      console.log(err);
      return;
    } else {
      res.redirect("/article/" + req.params.id);
    }
  });
});

// start server
app.listen(3000, () => {
  console.log("Server started on port 3000");
});
