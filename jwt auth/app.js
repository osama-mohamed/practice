const express = require("express");
const jwt = require("jsonwebtoken");
const port = process.env.PORT || 3000;
const app = express();

app.get("/api", (req, res) => {
  res.json({
    message: "Home page"
  });
});

app.post("/api/posts", verifyToken, (req, res) => {
  jwt.verify(req.token, "awesomeSecretKey", (err, auth) => {
    if (err) {
      res.json({
        message: "Auth faild!"
      });
    } else {
      res.json({
        message: "post created successfully!",
        auth
      });
    }
  });
});
app.post("/api/login", (req, res) => {
  const user = {
    id: 1,
    username: "osama mohamed",
    email: "osama6osama6@gmail.com"
  };
  jwt.sign(
    { user: user },
    "awesomeSecretKey",
    { expiresIn: "20m" },
    (err, token) => {
      res.json({
        message: "Loged in successfully!",
        token
      });
    }
  );
});

function verifyToken(req, res, next) {
  const header = req.headers.authorization;
  if (typeof header !== "undefined") {
    const newHeader = header.split(" ")[1];
    req.token = newHeader;
    next();
  } else {
    res.sendStatus(403);
  }
}

app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
