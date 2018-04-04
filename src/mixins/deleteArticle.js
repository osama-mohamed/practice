export default {
  methods: {
    deleteArticle (id) {
      this.articles.forEach(article => {
        if (article.id === id) {
          if (confirm(`Are you sure that you want to delete article ${article.title} ?`)){
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
        }
      })
    }
  }
}

