const express = require("express");
const router = express.Router();
const Idea = require("../models/Idea");

router.get("/", (req, res) => {
  Idea.find({})
    .sort({ date: "desc" })
    .then(ideas => {
      res.render("ideas/index", { ideas: ideas });
    });
});

router.get("/add", (req, res) => {
  res.render("ideas/add");
});

router.get("/edit/:id", (req, res) => {
  Idea.findOne({ _id: req.params.id }).then(idea => {
    res.render("ideas/edit", { idea: idea });
  });
});

router.post("/", (req, res) => {
  let errors = [];
  if (!req.body.title) {
    errors.push({ text: "Please add a title" });
  }
  if (!req.body.details) {
    errors.push({ text: "Please add some details" });
  }
  if (errors.length > 0) {
    res.render("ideas/add", {
      errors: errors,
      title: req.body.title,
      details: req.body.details
    });
  } else {
    const newIdea = {
      title: req.body.title,
      details: req.body.details
    };
    new Idea(newIdea).save().then(idea => {
      req.flash('success_msg', 'Saved successfully!');
      res.redirect("/ideas");
    });
  }
});

router.put("/:id", (req, res) => {
  Idea.findOne({ _id: req.params.id }).then(idea => {
    idea.title = req.body.title;
    idea.details = req.body.details;
    idea.save().then(idea => {
      req.flash('success_msg', 'Updated successfully!');
      res.redirect("/ideas");
    });
  });
});

router.delete("/:id", (req, res) => {
  Idea.deleteOne({ _id: req.params.id }).then(() => {
    req.flash('success_msg', 'Deleted successfully!');
    res.redirect("/ideas");
  });
});


module.exports = router;