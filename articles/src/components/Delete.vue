<template>
  <div>
  </div>
</template>

<script>
  export default {
    props: ['deleteArticleId', 'articlesArray'],
    watch: {
      'deleteArticleId': 'deleteArticle'
    },
    methods: {
      deleteArticle () {
        this.articlesArray.forEach(article => {
          if (article.id === this.deleteArticleId) {
            if (confirm(`Are you sure that you want to delete article ${article.title} ?`)){
              fetch(`http://localhost:8000/articles-api/delete/${this.deleteArticleId}/`, {
                method: 'delete'
              })
                .then(response => response)
                .then(res => {
                  alert('Article removed');
                  this.$parent.fetchArticles()
                })
                .catch(error => console.log(error))
            }
          }
        })
      },
    }
  }
</script>

<style scoped>

</style>
