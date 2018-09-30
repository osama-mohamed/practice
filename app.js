const express = require("express");
const bodyParser = require("body-parser");
const favicon = require("serve-favicon");
const path = require("path");
const mongoose = require("mongoose");
const session = require("express-session");
const expressValidator = require("express-validator");
const flash = require("connect-flash");
const passport = require("passport");
const config = require("./config/database");

// connect to database
mongoose.connect(
  config.database,
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

// bring in Article Model
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

// set favicon
app.use(favicon(path.join(__dirname, "public", "images", "favicon.ico")));
// app.use('/favicon.ico', express.static('images/favicon.ico'));
// app.use(favicon(__dirname + '/public/images/favicon.ico'));

// express session middleware
app.use(
  session({
    secret: "keyboard cat",
    resave: true,
    saveUninitialized: true
    // cookie: { secure: true }
  })
);

// express messages middleware
app.use(require("connect-flash")());
app.use(function(req, res, next) {
  res.locals.messages = require("express-messages")(req, res);
  next();
});

// Express Validator Middleware
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

// Passport Config
require("./config/passport")(passport);
// Passport Middleware
app.use(passport.initialize());
app.use(passport.session());

// Set user in var if the user logged in
app.get("*", async (req, res, next) => {
  res.locals.user = req.user || null;
  if (req.user) {
    await Article.find({ author: req.user._id }, (err, data) => {
      res.locals.userArticles = data;
    });
  }
  next();
});

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

// route files
let articles = require("./routes/articles");
let users = require("./routes/users");
app.use("/articles", articles);
app.use("/users", users);

// start server
app.listen(process.env.PORT || 3000, () => {
  console.log("Server started on port 3000");
});
