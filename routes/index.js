var express = require("express");
var router = express.Router();
var mongoose = require("mongoose");
mongoose.connect(
  "mongodb://localhost:27017/test",
  { useNewUrlParser: true }
);
var Schema = mongoose.Schema;

var userDataSchema = new Schema(
  {
    title: { type: String, required: true },
    content: { type: String, required: true },
    author: { type: String, required: true }
  },
  { collection: "user-data" }
);

var UserData = mongoose.model("UserData", userDataSchema);

/* GET home page. */
router.get("/", function(req, res, next) {
  res.render("index");
});

// retrive data
router.get("/get-data", function(req, res, next) {
  UserData.find().then(function(doc) {
    res.render("index", { items: doc });
  });
});

// insert data
router.post("/insert", function(req, res, next) {
  var item = {
    title: req.body.title,
    content: req.body.content,
    author: req.body.author
  };
  var data = new UserData(item);
  data.save();
  res.redirect("/");
});

// update data
router.post("/update", function(req, res, next) {
  var id = req.body.id;
  UserData.findById(id, function(err, doc) {
    if (err) {
      console.log("error, not saved");
    }
    doc.title = req.body.title;
    doc.content = req.body.content;
    doc.author = req.body.author;
    doc.save();
  });
  res.redirect("/");
});

// delete data
router.post("/delete", function(req, res, next) {
  var id = req.body.id;
  UserData.findOneAndDelete(id).exec();
  res.redirect("/");
});

module.exports = router;
