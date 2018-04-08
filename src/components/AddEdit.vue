<template>
  <div>
    <br>
    <h2 v-if="!update">Add Article</h2>
    <h2 v-if="update">{{update}} Article {{dropzoneOptions.params.title}}</h2>
    <br>
    <form @submit.prevent="addArticle" class="mb-4">
      <div class="form-group">
        <input type="text" class="form-control" v-model="dropzoneOptions.params.title" placeholder="Title" ref="title">
      </div>
      <div class="form-group">
        <textarea class="form-control" v-model="dropzoneOptions.params.body" placeholder="Body" ref="body"></textarea>
      </div>
      <div v-if="!update">
        <vueDropzone
          ref="myVueDropzoneref"
          id="myVueDropzone"
          :options="dropzoneOptions"
          @vdropzone-queue-complete="resetDropzone"
        ></vueDropzone>
      </div>
      <div v-if="update">
        <vueDropzone
          ref="myVueDropzoneref2"
          id="myVueDropzone"
          :options="dropzoneOptions2"
          @vdropzone-queue-complete="resetDropzone"
        ></vueDropzone>
      </div>
      <button type="submit" class="btn btn-success btn-block" v-if="!update">Add</button>
      <button type="submit" class="btn btn-success btn-block" v-if="update">{{update}}</button>
      <button type="button" v-if="update" @click="changeToAdd" class="btn btn-info btn-block mb-4">Click to change to add mode</button>
    </form>
  </div>
</template>


<script>
import vue2Dropzone from "vue2-dropzone";
import "vue2-dropzone/dist/vue2Dropzone.css";

let url = "http://localhost:8000/articles-api/new/";

export default {
  name: 'addedit',
  props: ['art'],
  watch: {
    'art': 'editArticle'
  },
  components: {
    vueDropzone: vue2Dropzone
  },
  data() {
    return {
      dropzoneOptions: {
        url: url,
        thumbnailWidth: 150,
        maxFilesize: 0.5,
        maxFiles: 1,
        addRemoveLinks: true,
        autoProcessQueue: false,
        params: {
          title: '',
          body: ''
        },
      },
      dropzoneOptions2: {
        url: url,
        dictDefaultMessage: "Update",
        thumbnailWidth: 150,
        maxFilesize: 0.5,
        maxFiles: 1,
        addRemoveLinks: true,
        autoProcessQueue: false,
        params: {
          title: '',
          body: ''
        },
      },
      article_id: '',
      edit: false,
      update: '',
    }
  },
  methods: {
    resetDropzone(){
      setTimeout(() => {
        alert(`Article ${this.dropzoneOptions.params.title} Added`)
        this.$refs.myVueDropzoneref.removeAllFiles(true)
        this.dropzoneOptions.params.title = ''
        this.dropzoneOptions.params.body = ''
        this.$parent.fetchArticles()
      }, 3000)
    },
    addArticle () {
      if (this.dropzoneOptions.params.title === '' ) {
        alert('Title must be filled')
        this.$refs.title.focus()
      } else if (this.dropzoneOptions.params.body === '') {
        alert('Body must be filled')
        this.$refs.body.focus()
      } else if (this.$refs.myVueDropzoneref.$el.dropzone.files[0] === undefined) {
        alert('Picture must be filled')
        document.getElementById('myVueDropzone').click()
      } else {
        if (this.edit === false) {
          this.$refs.myVueDropzoneref.processQueue()
        } else if (this.edit === true) {
          fetch(`http://localhost:8000/articles-api/update/${this.article_id}/`, {
            method: 'put',
            body: JSON.stringify(this.dropzoneOptions2.params),
            headers: {
              'content-type': 'application/json'
            }
          })
            .then(response => response.json())
            .then(data => {
              this.$refs.myVueDropzoneref2.processQueue()
              alert(`Article ${this.dropzoneOptions.params.title} Updated`)
              this.dropzoneOptions.params.title = ''
              this.dropzoneOptions.params.body = ''
              this.$refs.myVueDropzoneref2.removeAllFiles(true)
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
      this.article_id = this.art.id
      this.dropzoneOptions.params.title = this.art.title
      this.dropzoneOptions.params.body = this.art.body
      this.update = 'Update'
    },
    changeToAdd () {
      this.dropzoneOptions.params.title = ''
      this.dropzoneOptions.params.body = ''
      this.$refs.myVueDropzoneref.removeAllFiles(true)
      this.edit = false
      this.update = ''
      this.$parent.fetchArticles()
    }
  }
}
</script>


<style scoped>
#myVueDropzone{
  border-radius: .25rem;
  margin-bottom: 20px;
  min-height: 15px;
}
input,
textarea{
  text-align: center;
}
h2{
  text-align: center;
}
</style>
