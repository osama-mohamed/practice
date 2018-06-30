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
        <input type="file" id="newFile" v-on:change="fileChange($event.target.files)" ref="fileInput" class="form-control"/>
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
      // return this.$store.getters.userData
      // return this.$store.state.user.userData
      return this.$store.state.user.userData
    }
  },
  // computed: {
  //   user () {
  //     return this.$store.getters.userData
  //   }
  // },
  methods: {
    fileChange(fileList) {
      this.image = fileList[0]
    },
    onSubmit () {
      if (localStorage.getItem('userToken')) {
        if (this.image === null) {
          let newPost = {
            token: localStorage.getItem('userToken'),
            post: this.post
          }
          this.$store.dispatch('newPost', newPost)
        } else {
          const newPost = new FormData()
          newPost.append('token', localStorage.getItem('userToken'))
          newPost.append('post', this.post)
          newPost.append('file', this.image, this.image.name)
          this.$store.dispatch('newPost', newPost)
        }
        this.post = null
        this.image = null
        this.$refs.fileInput.type = 'text'
        this.$refs.fileInput.type = 'file'
      } else {
        this.$router.push({name: 'SignIn'})
      }
    }
  }
}
</script>

<style scoped>

</style>
