export default {
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
    }
  }
}

