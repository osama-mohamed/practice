export default {
  methods: {
    addArticle () {
      if (this.article.title == '') {
        alert('Title and body must be filled')
      } else {
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
              alert(`Article ${this.article.title} Added`)
              this.article.title = ''
              this.article.body = ''
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
              alert(`Article ${this.article.title} Updated`)
              this.article.title = ''
              this.article.body = ''
              this.edit = false
              this.update = ''
              this.fetchArticles()
            })
            .catch(error => console.log(error))
        }
      }
    }
  }
}
