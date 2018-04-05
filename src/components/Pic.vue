<template>
    <div>
      <br>
      <form enctype="multipart/form-data">
          <input type="file" name="file" v-on:change="fileChange($event.target.files)" />
          <input type="file" name="file" v-on:change="fileChange($event.target.files)" />
          <button type="button" v-on:click="upload()">Upload</button>
      </form>
    </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'apps',
  data() {
    return {
      files: new FormData()
    }
  },
  methods: {
    fileChange(fileList) {
      this.files.append("file", fileList[0], fileList[0].name);
    },
    upload() {
      axios({ method: "POST", "url": "http://localhost:8000/articles-api/new/", "data": this.files }).then(result => {
          console.dir(result.data);
      }, error => {
          console.error(error);
      });
    }
  }
}
</script>

<style scoped>

</style>
