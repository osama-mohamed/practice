<template>
  <div>
    <h2>Articles</h2>
    <nav aria-label="Page navigation example">
      <ul class="pagination">
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
      </ul>
    </nav>
    <div v-for="article in articles" v-bind:key="article.id" class="card card-body mb-2">
      <h3>{{article.title}}</h3>
      <p>{{article.body}}</p>
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
          console.log(res)
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
    }
  }
}
</script>

<style scoped>

</style>
