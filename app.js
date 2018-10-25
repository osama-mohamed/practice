const express = require("express");
const path = require("path");
const exphbs = require("express-handlebars");
const bodyParser = require("body-parser");
const methodOverride = require("method-override");
const flash = require("connect-flash");
const session = require("express-session");
const passport = require("passport");


const app = express();
const port = process.env.PORT || 3000;
require("dotenv").config();
require('./config/database');
require("./config/passport")(passport);



app.set("views", path.join(__dirname, "views"));
app.use(express.static(path.join(__dirname, "public")));
app.engine(
  "handlebars",
  exphbs({
    defaultLayout: "main"
  })
);
app.set("view engine", "handlebars");
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(methodOverride("_method"));
app.use(flash());
app.use(
  session({
    secret: "secretKey",
    resave: true,
    saveUninitialized: true
  })
);
app.use(passport.initialize());
app.use(passport.session());


app.use((req, res, next) => {
  res.locals.success_msg = req.flash("success_msg");
  res.locals.error_msg = req.flash("error_msg");
  res.locals.error = req.flash("error");
  res.locals.user = req.user || null;
  next();
});


const IdeasRoutes = require('./routes/ideas');
const UsersRoutes = require('./routes/users');
app.use('/ideas', IdeasRoutes);
app.use('/users', UsersRoutes);


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
