<template>
  <div>
    <input type="text" v-model="dropzoneOptions.params.title" placeholder="title">
    <input type="text" v-model="dropzoneOptions.params.body" placeholder="body">

    <vueDropzone
      ref="myVueDropzoneref"
      id="myVueDropzone"
      :options="dropzoneOptions"

      @vdropzone-queue-complete="resetDropzone"
    ></vueDropzone>
    <!--@vdropzone-complete="resetDropzone"-->
    <!--@vdropzone-success="resetDropzone"-->
    <!--@vdropzone-queue-complete="resetDropzone"-->
    <button @click="upload()">Please upload me</button>
    <p ref="compelete">{{dropzoneOptions.params}}</p>
  </div>
</template>

<script>
import vue2Dropzone from "vue2-dropzone";
import "vue2-dropzone/dist/vue2Dropzone.css";

let url = "http://localhost:8000/articles-api/new/";

export default {
  name: "test",
  components: {
    vueDropzone: vue2Dropzone
  },
  data() {
    return {
      dropzoneOptions: {
//        url: "https://httpbin.org/post",
         url: url,
        thumbnailWidth: 150,
        maxFilesize: 0.5,
        maxFiles: 1,
        addRemoveLinks: true,
//        uploadMultiple: true,
        autoProcessQueue: false, // this is to stop auto-upload // DOCS: http://www.dropzonejs.com/#config-autoProcessQueue
        params: {
          title: "",
          body: ""
        },
      }
    };
  },
  methods: {
    upload() {
      console.log("uploading ...");
      this.$refs.myVueDropzoneref.processQueue(); // this will start the upload
    },
    resetDropzone(){
      setTimeout(() => {
        this.dropzoneOptions.params.title = ''
        this.dropzoneOptions.params.body = ''
        this.$refs.myVueDropzoneref.removeAllFiles(true);
        this.$refs.compelete.textContent = 'Uploaded Successfully'
      }, 5000)
    }
  }
};
</script>

<style scoped>

</style>
