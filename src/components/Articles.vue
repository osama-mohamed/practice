<template>
  <div>
    <AddEdit v-on:newArticle="addArticle($event)"></AddEdit>


    <Delete v-bind:deleteArticleId="articleToDelete"  v-bind:articlesArray="articles"></Delete>
    <div v-for="article in articles" v-bind:key="article.id" class="card card-body mb-2">
      <h3>{{article.title}}</h3>
      <p>{{article.body}}</p>
      <hr>
      <button @click="editArticle(article)" class="btn btn-primary mb-2">Edit</button>
      <button @click="deleteArticleId(article.id)" class="btn btn-danger">Delete</button>
    </div>
  </div>
</template>

<script>
import AddEdit from './AddEdit.vue'
//import Pagination from './Pagination.vue'
import Delete from './Delete.vue'

export default {
  name: 'articles',
  components: {
    AddEdit,
//    Pagination,
    Delete
  },
  data () {
    return {
      articles: [],
      article: {
        id: '',
        title: '',
        body: ''
      },
      article_id: '',
      pagination: {},
      pagePagination: 5,
      edit: false,
      update: '',
      articleToDelete: ''
    }
  },
  created () {
    this.fetchArticles()
  },
  methods: {
    addArticle (article) {
      this.articles.push(article)
    },
    deleteArticleId(id) {
      this.articleToDelete = id
    },


    fetchArticles (page_url) {
      let vm = this
      page_url = page_url || 'http://localhost:8000/articles-api/all/'
      fetch(page_url)
        .then(response => response.json())
        .then(res => {
          this.articles = res.results
          vm.makePagination(res, res.next)
        })
        .catch(err => console.log(err))
    },
    makePagination (res, resh) {
      let paginate = {
        current_page: res.next,
        last_page: res.count,
        next_page_url: res.next,
        previous_page_url: res.previous
      }
      this.pagination = paginate
    },
    editArticle (article) {
      this.edit = true
      this.article.id = article.id
      this.article.article_id = article.id
      this.article.title = article.title
      this.article.body = article.body
      this.update = 'Update'
    },
    changeToAdd () {
      this.article.title = ''
      this.article.body = ''
      this.edit = false
      this.update = ''
      this.fetchArticles()
    }
  }
}
</script>

<style scoped>

</style>
