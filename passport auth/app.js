const express = require("express");
const path = require("path");
const cookieParser = require("cookie-parser");
const bodyParser = require("body-parser");
const expressHandlebars = require("express-handlebars");
const expressValidator = require("express-validator");
const flash = require("connect-flash");
const session = require("express-session");
const passport = require("passport");
const localStrategy = require("passport-local").Strategy;
const mongo = require("mongodb");
const mongoose = require("mongoose");
const port = process.env.PORT || 3000;
const app = express();
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

app.set("views", path.join(__dirname, "views"));
app.engine("handlebars", expressHandlebars({defaultLayout: 'layout'}));
app.set("view engine", "handlebars");
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, "public")));
app.use(
  session({
    secret: "secretKey",
    resave: true,
    saveUninitialized: true
    // cookie: { secure: true }
  })
);
app.use(passport.initialize());
app.use(passport.session());
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
app.use(flash());
app.use(function(req, res, next) {
  res.locals.success_msg = req.flash('success_msg');
  res.locals.error_msg = req.flash('error_msg');
  res.locals.error = req.flash('error'); // for passport errors
  res.locals.user = req.user || null;
  next();
});


const routes = require('./routes/index');
const users = require('./routes/users');
app.use('/', routes);
app.use('/users', users);


app.set('port', port);
app.listen(app.get('port'), () => {
  console.log(`Server started on port ${port}`);
});
