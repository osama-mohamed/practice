const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const path = require("path");
const app = express();
const port = process.env.PORT || 5000;

app.use(bodyParser.json());
app.use(cors());

const posts = require("./routes/api/posts");
app.use("/api/posts", posts);

// handle production
if (process.env.NODE_ENV === "production") {
  // handle static folder
  app.use(express.static(path.join(__dirname, "public")));
  // handle spa > vue
  app.get(/.*/, (req, res) => {
    res.sendFile(path.join(__dirname, "public/index.html"));
  });
}

app.listen(port, () => {
  console.log(`Server started on port ${port}.`);
});
