const express = require("express");
const path = require("path");
const router = express.Router();
const mongoose = require("mongoose");
const multer = require("multer");
const GridFsStorage = require("multer-gridfs-storage");
const Grid = require("gridfs-stream");
Grid.mongo = mongoose.mongo;
const crypto = require("crypto");

const databaseUrl = "mongodb://localhost:27017/mongouploads";
const conn = mongoose.createConnection(databaseUrl);
let gfs;


conn.once('open', () => {
  gfs = Grid(conn.db);
  gfs.collection('uploads');
});


const storage = new GridFsStorage({
  url: databaseUrl,
  file: (req, file) => {
    return new Promise((resolve, reject) => {
      crypto.randomBytes(16, (err, buf) => {
        if (err) {
          return reject(err);
        }
        const filename = buf.toString('hex') + path.extname(file.originalname);
        const fileInfo = {
          filename: filename,
          bucketName: 'uploads'
        };
        resolve(fileInfo);
      });
    });
  }
});
const upload = multer({ storage });


router.get("/", (req, res) => {
  gfs.files.find().toArray((err, files) => {
    if(!files || files.length == 0) {
      res.render("index", {files: false});
    } else {
      files.map(file => {
        if(file.contentType == "image/jpeg" || file.contentType == "image/png" ) {
          file.isImage = true;
        } else {
          file.isImage = false;
        }
      });
      res.render("index", {files: files});
    }
  });
});


router.get("/files", (req, res) => {
  gfs.files.find().toArray((err, files) => {
    if(!files || files.length == 0) {
      return res.sendStatus(404).json({
        err: 'No files exists'
      });
    }
    return res.json(files);
  });
});

router.get("/files/:filename", (req, res) => {
  gfs.files.findOne({filename: req.params.filename}, (err, file) => {
    if(!file || file.length == 0) {
      return res.json({
        err: 'No file exists'
      });
    }
    return res.json(file);
  });
});

router.get("/image/:filename", (req, res) => {
  gfs.files.findOne({filename: req.params.filename}, (err, file) => {
    if(!file || file.length == 0) {
      return res.json({
        err: 'No file exists'
      });
    }
    if(file.contentType == "image/jpeg" || file.contentType == "image/png" ) {
      const readstream = gfs.createReadStream(file.filename);
      readstream.pipe(res);
    } else {
      return res.json({
        err: 'Not an image'
      });
    }
  });
});


router.post("/upload", upload.single('file'), (req, res) => {
  res.redirect('/');
});



router.delete("/files/:id", (req, res) => {
  gfs.remove({_id: req.params.id, root: 'uploads'}, (err, gridStore) => {
    if(err) {
      return res.json({
        err: err
      });
    }
    return res.redirect('/');
  });
});


module.exports = router;
