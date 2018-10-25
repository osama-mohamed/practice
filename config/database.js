const mongoose = require("mongoose");


mongoose.Promise = global.Promise;
mongoose
  .connect(
    "mongodb://localhost:27017/videoidea",
    { useNewUrlParser: true }
  )
  .then(() => {
    console.log("MongoDB connected ...");
  })
  .catch(err => console.log(err));