const express = require("express");
const router = express.Router();
const passport = require("passport");
const LocalStrategy = require("passport-local").Strategy;
let User = require("../models/user");

router.get("/register", (req, res, next) => {
  res.render("register");
});

router.get("/login", (req, res, next) => {
  res.render("login");
});

router.post("/register", (req, res, next) => {
  const name = req.body.name;
  const username = req.body.username;
  const email = req.body.email;
  const password = req.body.password;
  const confirmPassword = req.body.confirmPassword;
  req.checkBody("name", "Name is required").notEmpty();
  req.checkBody("username", "Username is required").notEmpty();
  req.checkBody("email", "Email is required").notEmpty();
  req.checkBody("email", "Email is not valid").isEmail();
  req.checkBody("password", "Password is required").notEmpty();
  req.checkBody("confirmPassword", "Confirm Password is required").notEmpty();
  req
    .checkBody("confirmPassword", "Passwords does not matched")
    .equals(password);
  const errors = req.validationErrors();
  if (errors) {
    res.render("register", {
      errors: errors
    });
  } else {
    const newUser = new User({
      name,
      username,
      email,
      password
    });
    User.createUser(newUser, (err, user) => {
      if (err) throw err;
    });
    req.flash("success_msg", "You registered successfully!");
    res.redirect("/users/login");
  }
});

passport.use(
  new LocalStrategy(function(username, password, done) {
    User.getUserByUsername(username, (err, user) => {
      if (err) throw err;
      if (!user) {
        return done(null, false, { message: "Incorrect username." });
      }
      User.comparePassword(password, user.password, (err, isMatch) => {
        if (err) throw err;
        if (isMatch) {
          return done(null, user);
        } else {
          return done(null, false, { message: "Incorrect password." });
        }
      });
    });
  })
);

passport.serializeUser((user, done) => {
  done(null, user.id);
});

passport.deserializeUser((id, done) => {
  User.getUserById(id, (err, user) => {
    done(err, user);
  });
});

router.post(
  "/login",
  passport.authenticate("local", {
    // successRedirect: "/",
    failureRedirect: "/users/login",
    failureFlash: true
  }),
  (req, res) => {
    req.flash('success_msg', 'You logged in successfully!');
    res.redirect("/");
  }
);

router.get('/logout', (req, res) => {
  req.logout();
  req.flash('success_msg', 'You logged out successfully!');
  res.redirect('/users/login');
});

module.exports = router;
