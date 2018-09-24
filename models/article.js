let mongoose = require("mongoose");

// Articles Schema
let articleSchema = mongoose.Schema({
  title: {
    type: String,
    required: true
  },
  author: {
    type: String,
    required: true
  },
  body: {
    type: String,
    required: true
  },
  created: {
    type: Date
  },
  updated: {
    type: Date
  }
});

// export the model
let Article = module.exports = mongoose.model("Article", articleSchema);
