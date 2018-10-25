const express = require("express");
const path = require("path");
const mongoose = require("mongoose");
const exphbs = require("express-handlebars");
const bodyParser = require("body-parser");

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
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get("/", (req, res) => {
  const title = "Hello osama";
  res.render("index", {
    title: title
  });
});

app.get("/about", (req, res) => {
  res.render("about");
});

app.get("/ideas", (req, res) => {
  Idea.find({})
    .sort({ date: "desc" })
    .then(ideas => {
      res.render("ideas/index", { ideas: ideas });
    });
});

app.get("/ideas/add", (req, res) => {
  res.render("ideas/add");
});

app.get("/ideas/edit/:id", (req, res) => {
  Idea.findOne({_id: req.params.id}).then(idea => {
    res.render("ideas/edit", {idea: idea});
  });
});

app.post("/ideas", (req, res) => {
  let errors = [];
  if (!req.body.title) {
    errors.push({ text: "Please add a title" });
  }
  if (!req.body.details) {
    errors.push({ text: "Please add some details" });
  }
  if (errors.length > 0) {
    res.render("ideas/add", {
      errors: errors,
      title: req.body.title,
      details: req.body.details
    });
  } else {
    const newIdea = {
      title: req.body.title,
      details: req.body.details
    };
    new Idea(newIdea).save().then(idea => {
      res.redirect("/ideas");
    });
  }
});

app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
