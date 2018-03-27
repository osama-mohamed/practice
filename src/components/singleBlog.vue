<template>
  <div id="single-blog">
    <template v-if="!loading">
      <h1>{{blog.title}}</h1>
      <p>{{blog.author}}</p>
      <ul>
        <li v-for="category in blog.categories">{{category}}</li>
      </ul>
      <article>{{blog.body}}</article>
    </template>
    <p v-else>loading...</p>
    <br>
    <br>
    <button v-on:click="prev()" v-if="id > 1">Previous</button>
    <button v-on:click="next()" v-if="id < 100">Next</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      id: parseInt(this.$route.params.id),
      blog: {},
      loading: false
    };
  },
  created() {
    this.getData();
  },
  methods: {
    next: function() {
      if (this.id <= 100) {
        this.id += 1;
      }
      this.$router.push(`/blog/${this.id}`);
      this.getData();
    },
    prev: function() {
      if (this.id > 1) {
        this.id -= 1;
      }
      this.$router.push(`/blog/${this.id}`);
      this.getData();
    },
    getData: function() {
      this.loading = true;
      this.$http
        .get(`https://jsonplaceholder.typicode.com/posts/${this.id}`)
        .then(data => {
          this.blog = data.body;
          this.loading = false;
        })
        .catch(err => {
          this.loading = false;
          console.log(err);
        });
    }
  }
};
</script>

<style scoped>
#single-blog {
  max-width: 960px;
  margin: 0 auto;
}
</style>
