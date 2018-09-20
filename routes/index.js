var express = require("express");
var router = express.Router();

/* GET home page. */
router.get("/", function(req, res, next) {
  res.render("index", {
    title: "From Validation",
    success: req.session.success,
    errors: req.session.errors
  });
  req.session.errors = null;
  req.session.success = null;
});

/* check validity*/

router.post("/submit", function(req, res, next) {
  req.check("email", "Invalid email address").isEmail();
  req
    .check("password", "Password is invalid")
    .isLength({ min: 8 })
    .equals(req.body.confirmPassword);

  var errors = req.validationErrors();
  if (errors) {
    req.session.errors = errors;
    req.session.success = false;
  } else {
    req.session.success = true;
  }
  res.redirect("/");
});

module.exports = router;
