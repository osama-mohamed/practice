const mongoose = require("mongoose");

let MongoUrl = '';
if(process.env.NODE_ENV === 'production') {
  MongoUrl = process.env.MongoUrl;
} else {
  MongoUrl = "mongodb://localhost:27017/videoidea";
}


mongoose.Promise = global.Promise;
mongoose
  .connect(
    MongoUrl,
    { useNewUrlParser: true }
  )
  .then(() => {
    console.log("MongoDB connected ...");
  })
  .catch(err => console.log(err));