const multer = require("multer");

module.exports = function(req, err, numberOfFiles) {
  if (err) {
    if (err == "MulterError: Unexpected field") {
      return { msg: `Error: Files are more than ${numberOfFiles} !` };
    } else if (err instanceof multer.MulterError) {
      return { msg: "Error: Files are too Large!" };
    } else {
      return { msg: err };
    }
  } else {
    if (req.files == undefined || req.files == "") {
      return { msg: "Error: No Files Selected!" };
    } else {
      return { msg: "Files Uploaded" };
    }
  }
};
