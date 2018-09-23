const express = require("express");
const router = express.Router();

// bring in Article Model
let Article = require("../models/article");

// add new article route
router.get("/add", (req, res) => {
  res.render("add_article", {
    title: "Add Article"
  });
});

// add new article submit route
router.post("/add", (req, res) => {
  req.checkBody("title", "Title is required").notEmpty();
  req.checkBody("author", "Author is required").notEmpty();
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
    article.author = req.body.author;
    article.body = req.body.body;
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
router.get("/edit/:id", (req, res) => {
  Article.findById(req.params.id, (err, article) => {
    if (err) {
      console.log(err);
    } else {
      res.render("edit_article", {
        title: "Edit Article",
        article: article
      });
    }
  });
});

// save edited article
router.post("/edit/:id", (req, res) => {
  let article = {};
  article.title = req.body.title;
  article.author = req.body.author;
  article.body = req.body.body;

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
router.delete("/delete/:id", (req, res) => {
  let query = { _id: req.params.id };
  Article.remove(query, err => {
    if (err) {
      console.log(err);
      return;
    } else {
      req.flash("success", "Article Deleted Successfully!");
      res.send("Success");
    }
  });
});

// get article detail
router.get("/:id", (req, res) => {
  Article.findById(req.params.id, (err, article) => {
    if (err) {
      console.log(err);
    } else {
      res.render("article", {
        article: article
      });
    }
  });
});

module.exports = router;
