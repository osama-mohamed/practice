<template>
  <div>
    <AddEdit v-bind:art="articleToUpdate"></AddEdit>
    <Delete v-bind:deleteArticleId="articleToDelete"  v-bind:articlesArray="articles"></Delete>
    <Pagination v-bind:articleList="pag" v-on:paginationPages="page($event)"></Pagination>

    <div v-for="article in articles" v-bind:key="article.id" class="card card-body mb-2">
      <h3>{{article.title}}</h3>
      <p>Body : {{article.body}}</p>
      <img v-bind:src="article.img">
      <hr>
      <button @click="editArticle(article)" class="btn btn-primary mb-2">Edit</button>
      <button @click="deleteArticleId(article.id)" class="btn btn-danger">Delete</button>
    </div>
  </div>
</template>

<script>
import AddEdit from './AddEdit.vue'
import Pagination from './Pagination.vue'
import Delete from './Delete.vue'

export default {
  name: 'articles',
  components: {
    AddEdit,
    Pagination,
    Delete
  },
  data () {
    return {
      articles: [],
      articleToDelete: '',
      articleToUpdate: '',
      pag: [],
      numberOfArticles: ''
    }
  },
  created () {
    this.fetchArticles()
  },
  methods: {
    deleteArticleId(id) {
      this.articleToDelete = id
    },
    editArticle(article) {
      this.articleToUpdate = article
    },
    fetchArticles (page_url) {
      let vm = this
      page_url = page_url || 'http://localhost:8000/articles-api/all/'
      fetch(page_url)
        .then(response => response.json())
        .then(res => {
          this.articles = res.results
          this.pag = res
          this.numberOfArticles = res.count
        })
        .catch(err => console.log(err))
    },
    page (e) {
      this.fetchArticles(e)
    }
  }
}
</script>

<style scoped>
img{
  max-width: 85%;
  margin: 0 auto;
}
</style>
