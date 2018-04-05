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
      <div class="form-group">
        <input type="file" class="form-control" v-on:change="onFileChange" ref="fileupload">
      </div>
      <button type="submit" class="btn btn-success btn-block" v-if="!update">Add</button>
      <button type="submit" class="btn btn-success btn-block" v-if="update">{{update}}</button>
      <button type="button" v-if="update" @click="changeToAdd" class="btn btn-info btn-block mb-4">Click to change to add mode</button>
    </form>
  </div>
</template>


<script>
export default {
  name: 'addedit',
  props: ['art'],
  watch: {
    'art': 'editArticle'
  },
  data() {
    return {
      article: {
        id: '',
        title: '',
        body: '',
        img: ''
      },
      article_id: '',
      edit: false,
      update: '',
      fileSource: ''
    }
  },
  methods: {
    onFileChange(e) {
      this.fileSource = e.target.files[0].name || e.dataTransfer.files;
      this.article.img = this.fileSource;
    },
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
              this.$refs.fileupload.type = 'text'
              this.$refs.fileupload.type = 'file'
              this.$parent.fetchArticles()
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
              this.$refs.fileupload.type = 'text'
              this.$refs.fileupload.type = 'file'
              this.edit = false
              this.update = ''
              this.$parent.fetchArticles()
            })
            .catch(error => console.log(error))
        }
      }
    },
    editArticle () {
      this.edit = true
      this.article.id = this.art.id
      this.article.article_id = this.art.id
      this.article.title = this.art.title
      this.article.body = this.art.body
      this.update = 'Update'
    },
    changeToAdd () {
      this.article.title = ''
      this.article.body = ''
      this.$refs.fileupload.type = 'text'
      this.$refs.fileupload.type = 'file'
      this.edit = false
      this.update = ''
      this.$parent.fetchArticles()
    }
  }
}
</script>
