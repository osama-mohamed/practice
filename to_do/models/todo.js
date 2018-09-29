let mongoose = require("mongoose");

let todoSchema = mongoose.Schema({
  item: {
    type: String,
  },
  done: {
    type: Boolean,
  }
});

let Todo = module.exports = mongoose.model("Todo", todoSchema);