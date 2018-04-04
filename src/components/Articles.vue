<template>
  <div>
    <h2 v-if="!update">Add Article</h2>
    <h2 v-if="update">{{update}} Article {{article.title}}</h2>
    <form @submit.prevent="addArticle" class="mb-4">
      <div class="form-group">
        <input type="text" class="form-control" v-model="article.title" placeholder="Title">
      </div>
      <div class="form-group">
        <textarea class="form-control" v-model="article.body" placeholder="Body"></textarea>
      </div>
      <button type="submit" class="btn btn-success btn-block" v-if="!update">Add</button>
      <button type="submit" class="btn btn-success btn-block update" v-if="update">{{update}}</button>
      <button type="button" v-if="update" @click="changeToAdd" class="btn btn-info btn-block mb-4">Click to change to add mode</button>
    </form>
    <h2 class="text-center mb-4">Articles</h2>
    <nav aria-label="Page navigation example">
      <ul class="pagination">
        <li v-bind:class="[{disabled: !pagination.previous_page_url}]" class="page-item">
          <a class="page-link" href="#" @click.prevent="fetchArticles(pagination.previous_page_url.substring(0, pagination.previous_page_url.indexOf('l/')) + 'l/')">First Page</a>
        </li>

        <li v-bind:class="[{disabled: !pagination.previous_page_url}]" class="page-item">
          <a class="page-link" href="#" @click.prevent="fetchArticles(pagination.previous_page_url)">Previous</a>
        </li>
        <li class="page-item disabled" v-if="pagination.current_page">
          <a class="page-link text-dark" href="#">
            Page {{pagination.current_page.substring(pagination.current_page.indexOf('=') +1) -1}} of {{Math.round(pagination.last_page /pagePagination)}}</a>
            <!--Page {{pagination.current_page.substring(44 + 1) -1}} of {{Math.round(pagination.last_page /5)}}</a>-->
        </li>
        <li class="page-item disabled" v-else>
          <a class="page-link text-dark" href="#">
            Page {{Math.round(pagination.last_page /pagePagination)}} of {{Math.round(pagination.last_page /pagePagination)}}</a>
        </li>

        <li v-bind:class="[{disabled: !pagination.next_page_url}]" class="page-item">
          <a class="page-link" href="#" @click.prevent="fetchArticles(pagination.next_page_url)">Next</a>
        </li>


        <li v-bind:class="[{disabled: !pagination.next_page_url}]" class="page-item">
          <a class="page-link" href="#" @click.prevent="fetchArticles(pagination.next_page_url.substring(0, pagination.next_page_url.indexOf('=')) + '=' + Math.round(pagination.last_page/pagePagination))">Last Page</a>
        </li>
      </ul>
    </nav>
    <div v-for="article in articles" v-bind:key="article.id" class="card card-body mb-2">
      <h3>{{article.title}}</h3>
      <p>{{article.body}}</p>
      <hr>
      <button @click="editArticle(article)" class="btn btn-primary mb-2">Edit</button>
      <button @click="deleteArticle(article.id)" class="btn btn-danger">Delete</button>
    </div>
  </div>
</template>

<script>
import fetchArticles from '../mixins/fetchArticles'
import addArticle from '../mixins/addArticle'
import editArticle from '../mixins/editArticle'
import deleteArticle from '../mixins/deleteArticle'
import pagination from '../mixins/pagination'

export default {
  name: 'articles',
  mixins: [
    fetchArticles,
    addArticle,
    editArticle,
    deleteArticle,
    pagination,
  ],
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
      update: ''
    }
  },
  created () {
    this.fetchArticles()
  },
  methods: {

  }
}
</script>

<style scoped>

</style>
