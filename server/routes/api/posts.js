const express = require("express");
const mongodb = require("mongodb");
const router = express.Router();

async function loadPostsCollection() {
  const client = await mongodb.MongoClient.connect(
    "mongodb://localhost:27017/posts",
    { useNewUrlParser: true }
  );
  return client.db("posts").collection("posts");
}

router.get("/", async (req, res, next) => {
  const posts = await loadPostsCollection();
  res.send(await posts.find({}).toArray());
});

module.exports = router;
