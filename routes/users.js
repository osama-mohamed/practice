const express = require("express");
const router = express.Router();
const bcrypt = require("bcryptjs");

// bring in Article Model
let User = require("../models/user");

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
      password: password,
      confirmPassword: confirmPassword
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


// register form
router.get("/login", (req, res) => {
    res.render("login");
  });
module.exports = router;
