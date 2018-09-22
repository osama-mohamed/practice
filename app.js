const express = require("express");
const path = require("path");

// init app
const app = express();

// load view engine
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "pug");

// home route
app.get("/", (req, res) => {
  let articles = [
      {
          id: 1,
          title: 'Article one',
          author: 'OSAMA MOHAMED',
          body: 'This is article one'
      },
      {
          id: 2,
          title: 'Article two',
          author: 'OSAMA',
          body: 'This is article two'
      },
      {
          id: 3,
          title: 'Article three',
          author: 'OS',
          body: 'This is article three'
      },
  ];
  res.render("index", {
      title: 'Articles',
      articles: articles
  });
});

// add new article route
app.get("/articles/add", (req, res) => {
  res.render("add_article", {
      title: 'Add Article'
  });
});

// start server
app.listen(3000, () => {
  console.log("Server started on port 3000");
});
