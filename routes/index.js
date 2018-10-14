const express = require("express");
const router = express.Router();
const bcrypt = require("bcryptjs");
const passport = require("passport");

router.get("/", (req, res, next) => {
  res.render("index");
});

module.exports = router;
