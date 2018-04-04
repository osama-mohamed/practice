export default {
  methods: {
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
