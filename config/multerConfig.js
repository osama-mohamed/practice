const multer = require("multer");
const path = require("path");
// const numberOfFiles = 2;

module.exports = function(
  folderName = "defaultUploadsFolder",
  numberOfFiles = 2
) {
  // set storage engine
  const storage = multer.diskStorage({
    // file destination & path on req.file
    destination: path.join(__dirname, "../public", "uploads", folderName),
    filename: function(req, file, cb) {
      cb(
        null,
        file.fieldname + "-" + Date.now() + path.extname(file.originalname)
      );
    }
  });

  // init upload
  return multer({
    storage: storage,
    limits: { fileSize: 1000000 }, // size in bytes (1MB = 1000 * 1000 = 1000000)
    fileFilter: function(req, file, cb) {
      checkFileType(file, cb);
    }
  }).array("myImage", numberOfFiles);
};

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
