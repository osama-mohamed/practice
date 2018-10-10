<template>
  <div class="container">
    <h1>Latest Posts</h1>
    <div class="create-post">
      <label for="create-post">Write post: &emsp;</label>
      <input type="text" id="create-post" v-model="text" placeholder="Create a new post">
      &emsp;
      <button @click.enter="createPost">Post</button>
    </div>
    <hr>
    <h3 v-if="posts.length > 0 && posts.length!= 1">All Posts : {{ posts.length }} Posts</h3>
    <h3 v-else-if="posts.length == 1">Only one Post</h3>
    <h3 v-else-if="posts.length == 0">Please add post to show below.</h3>
    <p class="error" v-if="error">{{ error }}</p>
    <h4 v-if="posts.length > 0">To delete post : just double click on it</h4>
    <div class="posts-container">
      <div class="post"
        v-for="(post, index) in posts"
        :item="post._id"
        :index="index"
        :key="post._id"
        @dblclick="deletePost(post._id)">
        <div class="created-at">
          {{ `${post.createdAt.getDate()}/${post.createdAt.getMonth() + 1}/${post.createdAt.getFullYear()} ` }}
          {{ `${post.createdAt.getHours()}-${post.createdAt.getMinutes()}-${post.createdAt.getSeconds()}` }}
        </div>
        <div class="index">
          {{ post._id }}
        </div>
        <p class="text">{{ post.text }}</p>
      </div>
      
    </div>
  </div>
</template>

<script>
import PostService from "../PostService";

export default {
  name: "Post",
  data() {
    return {
      posts: [],
      error: "",
      text: ""
    };
  },
  async created() {
    try {
      this.posts = await PostService.getPosts();
    } catch (err) {
      this.error = err.message;
    }
  },
  methods: {
    async createPost() {
      await PostService.insertPost(this.text);
      this.text = "";
      this.posts = await PostService.getPosts();
    },
    async deletePost(id) {
      await PostService.deletePost(id);
      this.posts = await PostService.getPosts();
    }
  }
};
</script>

<style scoped>
div.container {
  max-width: 800px;
  margin: 0 auto;
}
p.error {
  border: 1px solid #ff5b5f;
  background-color: #ffc5c1;
  padding: 10px;
  margin-bottom: 15px;
}
div.post {
  position: relative;
  border: 1p solid #5bd658;
  background-color: #bcffb8;
  padding: 10px 10px 30px 10px;
  margin-bottom: 15px;
}
div.created-at,
div.index {
  position: absolute;
  top: 0;
  padding: 5px 15px 5px 15px;
  background-color: darkgreen;
  color: white;
  font-size: 13px;
}
div.created-at {
  left: 0;
}
div.index {
  right: 0;
}
p.text {
  font-size: 22px;
  font-weight: 700;
  margin-bottom: 0;
}
</style>
