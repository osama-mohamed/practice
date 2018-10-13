const express = require("express");
const mysql = require("mysql");
const db = mysql.createConnection({
  host: "localhost",
  user: "OSAMA",
  password: "OSAMA",
  database: "node_mysql"
});
db.connect(err => {
  if (err) throw err;
  console.log("Connected to MSQL");
});
const port = process.env.PORT || 3000;
const app = express();

app.get("/create-data-base", (req, res) => {
  const sql = "CREATE DATABASE node_mysql";
  db.query(sql, (err, result) => {
    if (err) throw err;
    res.send("DATABASE created ...");
  });
});

app.get("/create-posts-table", (req, res) => {
  const sql =
    "CREATE TABLE posts(id int AUTO_INCREMENT, title VARCHAR(255), body VARCHAR(255), PRIMARY KEY(id))";
  db.query(sql, (err, result) => {
    if (err) throw err;
    res.send("POSTS TABLE created ...");
  });
});

app.get("/create", (req, res) => {
  const post = {
    title: req.query.title,
    body: req.query.body
  };
  const sql = "INSERT INTO posts SET ?";
  db.query(sql, post, (err, result) => {
    if (err) throw err;
    res.send({
      message: "POST created ..."
    });
  });
});

app.get("/read", (req, res) => {
  const sql = "SELECT * FROM posts";
  db.query(sql, (err, posts) => {
    if (err) throw err;
    if (posts.length > 0) {
      res.send({
        message: "All posts fetched successfully!",
        posts
      });
    } else {
      res.send({
        message: "No posts yet"
      });
    }
  });
});

app.get("/read/:id", checkId, (req, res, next) => {
  const sql = `SELECT * FROM posts WHERE id = ${req.params.id}`;
  db.query(sql, (err, post) => {
    if (err) throw err;
    res.send({
      message: `post with id = ${req.params.id} fetched successfully!`,
      post: post.shift()
    });
  });
});

app.get("/update/:id", checkId, (req, res) => {
  const newPost = {
    title: req.query.title,
    body: req.query.body
  };
  const sql = `UPDATE posts SET title = '${newPost.title}', body = '${
    newPost.body
  }' WHERE id = ${req.params.id}`;
  db.query(sql, (err, post) => {
    if (err) throw err;
    res.send({
      message: `post with id = ${req.params.id} updated successfully!`
    });
  });
});

app.get("/delete/:id", checkId, (req, res) => {
  const sql = `DELETE FROM posts WHERE id = ${req.params.id}`;
  db.query(sql, (err, post) => {
    if (err) throw err;
    res.send({
      message: `post with id = ${req.params.id} deleted successfully!`
    });
  });
});

function checkId(req, res, next) {
  const sql = `SELECT * FROM posts WHERE id = ${req.params.id}`;
  db.query(sql, (err, post) => {
    if (err) throw err;
    if (post.length > 0) {
      next();
    } else {
      res.send({
        message: "No post with that id >_<"
      });
    }
  });
}
// app.get("/create", (req, res) => {
//   const post = {
//     title: "post title",
//     body: "post body text"
//   };
//   let sql = "INSERT INTO posts SET ?";
//   db.query(sql, post, (err, result) => {
//     if (err) throw err;
//     res.send({
//       message: "POST created ..."
//     });
//   });
// });

// app.get("/update/:id", (req, res) => {
//   const newPost = {
//     title: "post title updated",
//     body: "post body text updated"
//   };
//   let sql = `UPDATE posts SET title = '${newPost.title}', body = '${newPost.body}' WHERE id = ${req.params.id}`;
//   db.query(sql, (err, post) => {
//     if (err) throw err;
//     res.send({
//       message: `post with id = ${req.params.id} updated successfully!`
//     });
//   });
// });

app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
