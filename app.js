const express = require("express");
const path = require("path");
const port = process.env.PORT || 3000;
const app = express();
const numberOfFiles = 4;
const upload = require("./config/multerConfig")(
  "users_profiles",
  numberOfFiles
);
const multerError = require("./config/multerError");

app.set("view engine", "ejs");
app.use(express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {
  res.render("index", { files: "" });
});

app.post("/upload", (req, res) => {
  upload(req, res, err => {
    const errorMsg = multerError(req, err, numberOfFiles);
    const context = {
      msg: errorMsg.msg,
      files: ''
    };
    if (errorMsg.msg == "Files Uploaded") {
      context.filesInfo = JSON.stringify(req.files);
      context.files = req.files;
    }
    res.render("index", context);
  });
});

app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});

module.exports = {
  numberOfFiles: numberOfFiles
};
