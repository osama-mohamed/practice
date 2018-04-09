<template>
    <div>
      <br>
      <form enctype="multipart/form-data" method="post">
        <input type="text" name="title" v-model="title">
        <input type="text" name="body" v-model="body">
        <input type="file" name="file" v-on:change="fileChange($event.target.files)" ref="fileInput"/>
        <button type="submit" v-on:click.prevent="upload()">Upload</button>
      </form>
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
      selectedFile: null,
    }
  },
  methods: {
    fileChange(fileList) {
      this.selectedFile = fileList[0]
    },
    upload() {
      const pf = new FormData()
      pf.append('title', this.title)
      pf.append('body', this.body)
      pf.append('file', this.selectedFile, this.selectedFile.name)
      this.title = ''
      this.body = ''
      this.$refs.fileInput.type = 'text'
      this.$refs.fileInput.type = 'file'
      axios.post('http://localhost:8000/articles-api/new/', pf, {
        onUploadProgress: uploadEvent => {
          console.log('Upload Progress' + Math.round(uploadEvent.loaded / uploadEvent.total) * 100 + '%')
        }
      })
        .then(res => {
          console.log('axios res is : ', res)
        })
        .catch(error => {
          console.log('axios error is : ', error)
        })
    }
  }
}
</script>

<style scoped>

</style>
