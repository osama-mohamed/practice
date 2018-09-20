var express = require("express");
var router = express.Router();
var mongo = require("mongodb").MongoClient;
var objectId = require("mongodb").ObjectID;
var assert = require("assert");

var url = "mongodb://localhost:27017/";

/* GET home page. */
router.get("/", function(req, res, next) {
  res.render("index");
});

// retrive data
router.get("/get-data", function(req, res, next) {
  var resultArray = [];
  mongo.connect(
    url,
    function(err, db) {
      var dbn = db.db("test");
      assert.equal(null, err);
      var cursor = dbn.collection("user-data").find();
      cursor.forEach(
        function(doc, err) {
          assert.equal(null, err);
          resultArray.push(doc);
        },
        function() {
          db.close();
          console.log("Done!");
          res.render("index", { items: resultArray });
        }
      );
    }
  );
});

// insert data
router.post("/insert", function(req, res, next) {
  var item = {
    title: req.body.title,
    content: req.body.content,
    author: req.body.author
  };
  mongo.connect(
    url,
    function(err, db) {
      assert.equal(null, err);
      var dbn = db.db("test");
      dbn.collection("user-data").insertOne(item, function(err, result) {
        assert.equal(null, err);
        console.log("Item inserted");
        db.close();
      });
    }
  );
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
  mongo.connect(
    url,
    function(err, db) {
      assert.equal(null, err);
      var dbn = db.db("test");
      dbn
        .collection("user-data")
        .updateOne({ _id: objectId(id) }, { $set: item }, function(
          err,
          result
        ) {
          assert.equal(null, err);
          console.log("Item updated");
          db.close();
        });
    }
  );
  res.redirect("/");
});

// delete data
router.post("/delete", function(req, res, next) {
  var id = req.body.id;
  mongo.connect(
    url,
    function(err, db) {
      assert.equal(null, err);
      var dbn = db.db("test");
      dbn
        .collection("user-data")
        .deleteOne({ _id: objectId(id) }, function(err, result) {
          assert.equal(null, err);
          console.log("Item deleted");
          db.close();
        });
    }
  );
  res.redirect("/");
});

module.exports = router;
