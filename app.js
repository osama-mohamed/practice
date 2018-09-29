const express = require("express");
const multer = require("multer");
const ejs = require("ejs");
const path = require("path");
const port = process.env.PORT || 3000;
const app = express();
const numberOfFiles = 2;

app.set("view engine", "ejs");
app.use(express.static(path.join(__dirname, "public")));

// set storage engine
const storage = multer.diskStorage({
  // file destination & path on req.file
  destination: path.join(__dirname, "public", "uploads"),
  filename: function(req, file, cb) {
    cb(
      null,
      file.fieldname + "-" + Date.now() + path.extname(file.originalname)
    );
  }
});

// init upload
const upload = multer({
  storage: storage,
  limits: { fileSize: 1000000 }, // size in bytes (1MB = 1000 * 1000 = 1000000)
  fileFilter: function(req, file, cb) {
    checkFileType(file, cb);
  }
}).array("myImage", numberOfFiles);

// check File Type
function checkFileType(file, cb) {
  const fileTypes = /jpeg|jpg|png|gif/; // allowed ext
  const extName = fileTypes.test(path.extname(file.originalname).toLowerCase()); // check ext
  const mimeType = fileTypes.test(file.mimetype); // check mime
  if (extName && mimeType) {
    return cb(null, true);
  } else {
    return cb("Error: Images Only!");
  }
}

app.get("/", (req, res) => {
  res.render("index", {files: ''});
});

app.post("/upload", (req, res) => {
  upload(req, res, err => {
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
