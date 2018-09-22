var express = require("express");
var bodyParser = require("body-parser");
var path = require("path");
var expressValidator = require("express-validator");
var mongojs = require("mongojs");
var db = mongojs('test', ["users"]);

var app = express();

/* var logger = function(req, res, next) {
  console.log("Logging ...");
  next();
};

app.use(logger); */

// view engine
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

// body parser middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

// static path
app.use(express.static(path.join(__dirname, "public")));

// global vars
app.use(function(req, res, next) {
  res.locals.errors = null;
  next();
});

// express-validator middleware options
app.use(
  expressValidator({
    errorFormatter: function(param, msg, value) {
      var namespace = param.split("."),
        root = namespace.shift(),
        formParam = root;

      while (namespace.length) {
        formParam += "[" + namespace.shift() + "]";
      }
      return {
        param: formParam,
        msg: msg,
        value: value
      };
    }
  })
);


app.get("/", function(req, res) {
  db.users.find(function(err, docs) {
    console.log(docs);
    res.render("index", {
      title: "Customers",
      users: docs
    });
  });
});

app.post("/users/add", function(req, res) {
  req.checkBody("first_name", "First name is required").notEmpty();
  req.checkBody("last_name", "Last name is required").notEmpty();
  req.checkBody("email", "Email is required").notEmpty();

  var errors = req.validationErrors();

  if (errors) {
    console.log("error", errors);
    res.render("index", {
      title: "Customers",
      users: users,
      errors: errors
    });
  } else {
    var newUser = {
      first_name: req.body.first_name,
      last_name: req.body.last_name,
      email: req.body.email
    };
    console.log("new", newUser);
    res.redirect("/");
  }
});

app.listen(3000, function() {
  console.log("Server started on port 3000 ...");
});
