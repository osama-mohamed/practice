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
      <!-- <div class="form-group">
        <label for="password">Password</label>
        <input v-model="password" autocomplete="off" required type="password" class="form-control" id="password" placeholder="Password">
      </div> -->
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
    onSubmit () {
      if (sessionStorage.getItem('userToken')) {
        let newPost = {
          token: sessionStorage.getItem('userToken'),
          post: this.post,
        }
        // console.log(newPost)
        this.post = null
        // this.$store.dispatch('newPost', newPost)
      } else {
        this.$router.push({name: 'SignIn'})
      }
    }
  }
}
</script>

<style scoped>

</style>
