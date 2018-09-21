var express = require("express");
var router = express.Router();
var db = require("monk")("localhost:27017/test");
var userData = db.get("user-data");

/* GET home page. */
router.get("/", function(req, res, next) {
  res.render("index");
});

// retrive data
router.get("/get-data", function(req, res, next) {
  var data = userData.find({});
  data.then(function(docs) {
    res.render("index", { items: docs });
  });
});

// insert data
router.post("/insert", function(req, res, next) {
  var item = {
    title: req.body.title,
    content: req.body.content,
    author: req.body.author
  };
  userData.insert(item);
  res.redirect("/");
});

// update data
router.post("/update", function(req, res, next) {
  var id = req.body.id;
  var item = {
    title: req.body.title,
    content: req.body.content,
    author: req.body.author
  };
  userData.update({"_id": db.id(id)}, item);
  // userData.updateById(id, item);
  res.redirect("/");
});

// delete data
router.post("/delete", function(req, res, next) {
  var id = req.body.id;
  userData.remove({"_id": db.id(id)});
  // userData.removeById(id);
  res.redirect("/");
});

module.exports = router;
