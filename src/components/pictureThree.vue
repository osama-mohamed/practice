<template>
    <div>
      <br>
      <!--<form enctype="multipart/form-data" method="post">-->
        <input type="text" name="title" v-model="title">
        <input type="text" name="body" v-model="body">
        <input type="file" name="file" v-on:change="fileChange($event.target.files)" ref="fileInput"/>
        <button type="button" v-on:click.prevent="upload()">Upload</button>
        <!--<button type="submit" v-on:click.prevent="upload()">Upload</button>-->
      <!--</form>-->
    </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'apps',
  data() {
    return {
      title: '',
      body: '',
      files: new FormData(),
    }
  },
  methods: {
    fileChange(fileList) {
      this.files.append("file", fileList[0], fileList[0].name);
    },
    upload() {
      this.files.append('title', this.title)
      this.files.append('body', this.body)
      this.title = ''
      this.body = ''
      this.$refs.fileInput.type = 'text'
      this.$refs.fileInput.type = 'file'
      let url = 'http://localhost:8000/articles-api/new/'
      this.axios.post(url, this.files, /*{
        headers: {
          'accept': 'application/json',
          'Accept-Language': 'en-US,en;q=0.8',
          'Content-Type': `multipart/form-data; boundary=${this.files._boundary}`,
        }
      }*/).then(res => {
        console.log(res)
      }).catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style scoped>

</style>
