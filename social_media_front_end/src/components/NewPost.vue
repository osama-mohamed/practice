<template>
  <div>
    <div v-if="user">
      <h1 class="text-center">New Post</h1>
    </div>
    <form @submit.prevent="onSubmit()">
      <div class="form-group">
        <label for="newPost">New Post</label>
        <textarea v-model="post" required id="newPost" class="form-control" autocomplete="off"></textarea>
      </div>
      <div class="form-group">
        <label for="newFile">File</label>
        <input v-on:change="fileChange($event.target.files)" type="file" class="form-control" id="newFile">
      </div>
      <button type="submit" class="btn btn-primary" >Post</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'newPost',
  data () {
    return {
      post: null,
      selectedFile: null,
      imageUrl: null,
      image: null,
    }
  },
  created() {
    this.user
  },
  computed: {
    user () {
      // console.log(this.$store.getters.userData)
      // console.log(this.$store.state.user.userData)
      return this.$store.getters.userData
      // return this.$store.state.user.userData
    }
  },
  methods: {
    fileChange (e) {
      // this.selectedFile = fileList[0]
      // console.log(this.selectedFile)
      const files = event.target.files
      let filename = files[0].name
      if (filename.lastIndexOf('.') <= 0) {
        return alert('Choose a valid file!')
      }
      const fileReader = new FileReader()
      fileReader.addEventListener('load', () => {
        this.imageUrl = fileReader.result
      })
      fileReader.readAsDataURL(files[0])
      this.image = files[0]
      console.log(files)
      console.log(filename)
      console.log(fileReader)
      console.log(this.imageUrl)
      console.log(this.image)
    },
    onSubmit () {
      if (sessionStorage.getItem('userToken')) {
        // console.log(this.$refs.file.files[0])
        let newPost = {
          token: sessionStorage.getItem('userToken'),
          post: this.post,
          file: this.imageUrl,
        }
        this.post = null
        this.$store.dispatch('newPost', newPost)
      } else {
        this.$router.push({name: 'SignIn'})
      }
    }
  }
}
</script>

<style scoped>

</style>
