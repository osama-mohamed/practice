<template>
   <div id="show-blogs">
     <h1>All Articles</h1>
     <input type="text" v-model="search" placeholder="Search Articles">
     <div v-for="blog in filteredBlogs" class="single-article">
        <router-link v-bind:to="'/blog/' + blog.id"><h2>{{ blog.title}}</h2></router-link>
        <article>{{ blog.body }}</article>
     </div>
   </div>
</template>

<script>
import searchMixin from '../mixins/searchMixin'

export default {
  data () {
    return {
      blogs: [],
      search: ''
    }
  },
  methods: {
  },
  computed: {

  },
  created() {
    this.$http.get('https://jsonplaceholder.typicode.com/posts').then(function (data) {
      this.blogs = data.body.slice(0, 12)
    })
  },
  mixins: [
    searchMixin
  ]
}
</script>

<style scoped>
#show-blogs{
    max-width: 800px;
    margin: 0 auto;
}
.single-article{
    padding: 20px;
    margin: 20px 0;
    box-sizing: border-box;
    background: #eee;
}
</style>
