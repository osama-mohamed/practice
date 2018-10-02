const express = require("express");
const ejs = require("ejs");
const multer = require("multer");
const path = require("path");
const port = process.env.PORT || 3000;
const app = express();
const numberOfFiles = 3;
const uploadFile = require('./config/multerConfig')('users_profiles', numberOfFiles);

app.set("view engine", "ejs");
app.use(express.static(path.join(__dirname, "public")));


app.get("/", (req, res) => {
  res.render("index", {files: ''});
});

app.post("/upload", (req, res) => {
  uploadFile(req, res, err => {
    if (err) {
      if (err == 'MulterError: Unexpected field') {
        res.render("index", {
          msg: `Error: Files are more than ${numberOfFiles}!`,
          files: ''
        });
      } else if (err instanceof multer.MulterError) {
        res.render("index", {
          msg: "Error: Files are too Large!",
          files: ''
        });
      } else {
        res.render("index", {
          msg: err,
          files: ''
        });
      }
    } else {
      if (req.files == undefined || req.files == '') {
        res.render("index", {
          msg: "Error: No Files Selected!",
          files: ''
        });
      } else {
        res.render("index", {
          msg: "Files Uploaded",
          filesInfo: JSON.stringify(req.files),
          files: req.files
        });
      }
    }
  });
});

app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
