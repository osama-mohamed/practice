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
  const allPosts = await posts.find({}).toArray();
  res.send({ posts: allPosts, count: allPosts.length });
});

router.post("/", async (req, res, next) => {
  const posts = await loadPostsCollection();
  await posts.insertOne({
    text: req.body.text,
    createdAt: new Date()
  });
  res.status(201).send({ message: "Post created successfully!" });
});

router.delete("/:id", async (req, res, next) => {
  const posts = await loadPostsCollection();
  await posts.deleteOne({ _id: new mongodb.ObjectID(req.params.id) });
  res.status(200).send({ message: "Post deleted successfully!" });
});
module.exports = router;
