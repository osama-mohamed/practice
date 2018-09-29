let Todo = require("../models/todo");

module.exports = app => {
  app.get("/", (req, res) => {
    Todo.find({}, (err, data) => {
      if (err) throw err;
      let doneTodos = 0;
      for (let x = 0; x < data.length; x++) {
        if (data[x].done === true) {
          doneTodos += 1;
        }
      }
      res.render("todo", { todos: data, doneTodos: doneTodos });
    });
  });

  app.post("/", (req, res) => {
    Todo({ item: req.body.item, done: false }).save((err, data) => {
      if (err) throw err;
      res.json(data);
    });
  });

  app.delete("/:item", (req, res) => {
    Todo.find({ item: req.params.item.replace(/-/g, " ") }).deleteOne(
      (err, data) => {
        if (err) throw err;
        res.json(data);
      }
    );
  });

  app.post("/done/:item", (req, res) => {
    let item = req.params.item.replace(/-/g, " ");
    Todo.findOne({ item: item }, (err, data) => {
      if (err) throw err;
      if (data.done === true) {
        let newItem = { item: item, done: false };
        Todo.updateOne({ item: item }, newItem, err => {
          if (err) throw err;
          res.json(data);
        });
      } else {
        let newItem = { item: item, done: true };
        Todo.updateOne({ item: item }, newItem, err => {
          if (err) throw err;
          res.json(data);
        });
      }
    });
  });
};
