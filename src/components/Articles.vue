<template>
  <div>
    <h2>Articles</h2>
    <form @submit.prevent="addArticle" class="mb-4">
      <div class="form-group">
        <input type="text" class="form-control" v-model="article.title" placeholder="Title">
      </div>
      <div class="form-group">
        <textarea class="form-control" v-model="article.body" placeholder="Body"></textarea>
      </div>
      <button type="submit" class="btn btn-success btn-block">Save</button>
    </form>
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
            Page {{pagination.current_page.substring(pagination.current_page.indexOf('=') +1) -1}} of {{Math.round(pagination.last_page /5)}}</a>
            <!--Page {{pagination.current_page.substring(44 + 1) -1}} of {{Math.round(pagination.last_page /5)}}</a>-->
        </li>
        <li class="page-item disabled" v-else>
          <a class="page-link text-dark" href="#">
            Page {{Math.round(pagination.last_page /5)}} of {{Math.round(pagination.last_page /5)}}</a>
        </li>

        <li v-bind:class="[{disabled: !pagination.next_page_url}]" class="page-item">
          <a class="page-link" href="#" @click.prevent="fetchArticles(pagination.next_page_url)">Next</a>
        </li>


        <li v-bind:class="[{disabled: !pagination.next_page_url}]" class="page-item">
          <a class="page-link" href="#" @click.prevent="fetchArticles(pagination.next_page_url.substring(0, pagination.next_page_url.indexOf('=')) + '=' + Math.round(pagination.last_page/5))">Last Page</a>
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
export default {
  name: 'articles',
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
      edit: false
    }
  },
  created () {
    this.fetchArticles()
  },
  methods: {
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
    deleteArticle (id) {
      if (confirm('Are you sure ?')){
        fetch(`http://localhost:8000/articles-api/delete/${id}/`, {
          method: 'delete'
        })
          .then(response => response)
          .then(res => {
            alert('Article removed');
            this.fetchArticles();
          })
          .catch(error => console.log(error))
      }
    },
    addArticle () {
      if (this.edit === false) {
        fetch('http://localhost:8000/articles-api/new/', {
          method: 'post',
          body: JSON.stringify(this.article),
          headers: {
            'content-type': 'application/json'
          }
        })
          .then(response => response.json())
          .then(data => {
            this.article.title = ''
            this.article.body = ''
            alert('Article Added')
            this.fetchArticles()
          })
          .catch(error => console.log(error))
      } else if (this.edit === true) {
        fetch(`http://localhost:8000/articles-api/update/${this.article.id}/`, {
          method: 'put',
          body: JSON.stringify(this.article),
          headers: {
            'content-type': 'application/json'
          }
        })
          .then(response => response.json())
          .then(data => {
            this.article.title = ''
            this.article.body = ''
            this.edit = false
            alert('Article Updated')
            this.fetchArticles()
          })
          .catch(error => console.log(error))
      }
    },
    editArticle (article) {
      this.edit = true
      this.article.id = article.id
      this.article.article_id = article.id
      this.article.title = article.title
      this.article.body = article.body
    }
  }
}
</script>

<style scoped>

</style>
