const express = require("express");
const router = express.Router();
const bcrypt = require("bcryptjs");
const passport = require("passport");

// bring in Article Model
let User = require("../models/user");
let Article = require("../models/article");

// register form
router.get("/register", (req, res) => {
  res.render("register");
});

// register submit
router.post("/register", (req, res) => {
  const name = req.body.name;
  const email = req.body.email;
  const username = req.body.username;
  const password = req.body.password;
  const confirmPassword = req.body.confirmPassword;

  req.checkBody("name", "Name is required").notEmpty();
  req.checkBody("email", "Email is required").notEmpty();
  req.checkBody("email", "Email is not valid").isEmail();
  req.checkBody("username", "Username is required").notEmpty();
  req.checkBody("password", "Password is required").notEmpty();
  req.checkBody("confirmPassword", "Confirm Password is required").notEmpty();
  req.checkBody("confirmPassword", "Passwords do not match").equals(password);

  let errors = req.validationErrors();
  if (errors) {
    res.render("register", {
      errors: errors
    });
  } else {
    let newUser = new User({
      name: name,
      email: email,
      username: username,
      password: password
    });

    bcrypt.genSalt(10, (err, salt) => {
      bcrypt.hash(newUser.password, salt, (err, hash) => {
        if (err) {
          console.log(err);
        }
        newUser.password = hash;
        newUser.save(error => {
          if (err) {
            console.log(err);
            return;
          } else {
            req.flash("success", "Successfully registered!");
            res.redirect("/users/login");
          }
        });
      });
    });
  }
});

// login form
router.get("/login", (req, res) => {
  res.render("login");
});

// login submit
router.post("/login", (req, res, next) => {
  passport.authenticate("local", {
    successRedirect: "/",
    failureRedirect: "/users/login",
    failureFlash: true
  })(req, res, next);
});

// logout
router.get("/logout", (req, res, next) => {
  req.logout();
  req.flash("success", "You logged out successfully!");
  res.redirect("/users/login");
});

// delete account
router.post("/delete-account", (req, res, next) => {
  Article.deleteMany({ author: req.user._id }, err => {
    if (err) {
      console.log(err);
      return;
    } else {
      User.deleteOne({ _id: req.user._id }, err => {
        if (err) {
          console.log(err);
          return;
        }
        res.send("Success");
      });
    }
  });
});

module.exports = router;
