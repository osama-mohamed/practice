<template>
  <div id="single-blog">
    <template v-if="!loading">
      <h1>{{blog.title}}</h1>
      <p>{{blog.author}}</p>
      <ul>
        <li v-for="category in blog.categories">{{category}}</li>
      </ul>
      <article>{{blog.content}}</article>
    </template>
    <p v-else>loading...</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      id: this.$route.params.id,
      blog: {},
      loading: false
    };
  },
  created() {
    this.getData();
  },
  methods: {
    getData: function() {
      this.loading = true;
      this.$http
        .get(`https://vue-app-osama.firebaseio.com/blog-posts/${this.id}.json`)
        .then(data => {
          return data.json();
        })
        .then(data => {
          this.blog = data;
          this.loading = false;
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
