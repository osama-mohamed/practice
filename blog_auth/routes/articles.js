const express = require("express");
const router = express.Router();

// Article Model
let Article = require("../models/article");
// User Model
let User = require("../models/user");

// add new article route
router.get("/add", ensureAuthenticated, (req, res) => {
  res.render("add_article", {
    title: "Add Article"
  });
});

// add new article submit route
router.post("/add", ensureAuthenticated, (req, res) => {
  req.checkBody("title", "Title is required").notEmpty();
  // req.checkBody("author", "Author is required").notEmpty();
  req.checkBody("body", "Body is required").notEmpty();

  //   get errors
  let errors = req.validationErrors();
  if (errors) {
    res.render("add_article", {
      title: "Add Article",
      errors: errors
    });
  } else {
    let article = new Article();
    article.title = req.body.title;
    // article.author = req.body.author;
    article.author = req.user._id;
    article.body = req.body.body;
    article.created = new Date();
    article.save(err => {
      if (err) {
        console.log(err);
        return;
      } else {
        req.flash("success", "Article Added Successfully!");
        res.redirect("/");
      }
    });
  }
});

// load edit article foarm
router.get("/edit/:id", ensureAuthenticated, (req, res) => {
  Article.findById(req.params.id, (err, article) => {
    if (err) {
      console.log(err);
    } else {
      if (article.author != req.user._id) {
        req.flash("danger", "Not authorized");
        res.redirect("/");
      } else {
        res.render("edit_article", {
          title: "Edit Article",
          article: article
        });
      }
    }
  });
});

// save edited article
router.post("/edit/:id", ensureAuthenticated, (req, res) => {
  let article = {};
  article.title = req.body.title;
  article.author = req.body.author;
  article.body = req.body.body;
  article.updated = new Date();

  let query = { _id: req.params.id };
  Article.updateOne(query, article, err => {
    if (err) {
      console.log(err);
      return;
    } else {
      req.flash("success", "Article Updated Successfully!");
      res.redirect("/articles/" + req.params.id);
    }
  });
});

// delete article
router.delete("/delete/:id", ensureAuthenticated, (req, res) => {
  if (!req.user._id) {
    res.status(500).send();
  }
  let query = { _id: req.params.id };

  Article.findById(req.params.id, (err, article) => {
    if (article.author != req.user._id) {
      res.status(500).send();
    } else {
      Article.deleteOne(query, err => {
        if (err) {
          console.log(err);
          return;
        } else {
          req.flash("success", "Article Deleted Successfully!");
          res.send("Success");
        }
      });
    }
  });
});

// get article detail
router.get("/:id", (req, res) => {
  Article.findById(req.params.id, (err, article) => {
    if (err) {
      console.log(err);
    } else {
      User.findById(article.author, (err, user) => {
        res.render("article", {
          article: article,
          author: user.name
        });
      });
    }
  });
});

// Access Control
function ensureAuthenticated(req, res, next) {
  if (req.isAuthenticated()) {
    return next();
  } else {
    req.flash("danger", "Please Login First!");
    res.redirect("/users/login");
  }
}
module.exports = router;
