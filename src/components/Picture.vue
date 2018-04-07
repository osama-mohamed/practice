<!--<template>
    <div>
      <br>
      <form enctype="multipart/form-data">
        <input type="text" name="title" v-model="title">
        <input type="text" name="body" v-model="body">
        <input type="file" name="file" v-on:change="fileChange($event.target.files)" />
        <button type="submit" v-on:click.prevent="upload()">Upload</button>
      </form>
    </div>
</template>

<script>
export default {
  name: 'apps',
  data() {
    return {
      title: '',
      body: '',
      files: new FormData()
    }
  },
  methods: {
    fileChange(fileList) {
      this.files.append("file", fileList[0], fileList[0].name);
    },
    upload() {
      let url = 'http://localhost:8000/articles-api/new/'
      let data = {
        img: this.files,
        title: this.title,
        body: this.body
      }

      this.axios.post(url, data, {
        headers: {
          'accept': 'application/json',
          'Accept-Language': 'en-US,en;q=0.8',
          'Content-Type': `multipart/form-data; boundary=${this.files._boundary}`,
        }
      }).then(res => {
        console.log(data)
        console.log(res)
      }).catch(err => {
        console.log(err)
      })

    }
  }
}
</script>

<style scoped>

</style>-->


<!--                                                          -->
<template>
  <div>
    <p>{{article.title}}</p>
    <p>{{article.body}}</p>
    <form>
      <input type="text" v-model="article.title">
      <input type="text" v-model="article.body">
      <vue-dropzone ref="myVueDropzone" id="dropzone" :options="dropzoneOptions" v-on:vdropzone-sending="sendingEvent"></vue-dropzone>
    </form>
  </div>
</template>

<script>
  import vue2Dropzone from 'vue2-dropzone'
  import 'vue2-dropzone/dist/vue2Dropzone.css'

  let url = 'http://localhost:8000/articles-api/new/'

  export default{
    name: 'test',
    components: {
      vueDropzone: vue2Dropzone
    },
    data() {
      return {
        article: {
          title: '',
          body: '',
        },
        dropzoneOptions: {
//            url: 'https://httpbin.org/post',
            url: url,
            thumbnailWidth: 150,
            maxFilesize: 0.5,
            addRemoveLinks: true,
//            dictDefaultMessage: "UPLOAD"
//            headers: { "My-Awesome-Header": "header value" }
            params: {
              title: this.title,
              body: this.body
            }
        },
      }
    },
    methods: {
      sendingEvent () {
        console.log(this.article.title)
        console.log(this.article.body)
        this.article.title = this.title
        this.article.body = this.body
//        this.title = title
//        this.body = body
      }
    }
  }
</script>



<!--
<template>
  <div>
    <form class="dropzone" id="my-awesome-dropzone" method="post" enctype="multipart/form-data" action="http://localhost:8000/articles-api/new/">
      <input name="file" type="file" multiple />
    </form>
  </div>
</template>
-->
