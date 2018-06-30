<template>
  <div v-if="user">
    <div>
      <h1 class="text-center">Profile</h1>
      <h2 class="text-center">{{user}}</h2>

      <div v-for="post in posts" :key="post.id" class="card" style="width: 49%;">
        <img class="card-img-top" v-if="post.image" :src="'static/uploads/' + post.image" :alt="post.post">
        <div class="card-body">
          <h5 class="card-title">#{{post.id}}</h5>
          <h5 class="card-title">{{post.added}}</h5>
          <h5 class="card-title">{{post.updated}}</h5>
          <p class="card-text">{{post.post}}</p>
          <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
        </div>
      </div>
      <!-- <ul v-for="post in posts" :key="post.id">
        <li>{{post.id}}</li>
        <li>{{post.post}}</li>
        <li>{{post.image}}</li>
      </ul> -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'Profile',
  data () {
    return {
      posts: [],
    }
  },
  created() {
    this.profile()
    this.profilePosts
  },
  computed: {
    user () {
      // console.log(this.$store.getters.userData)
      // console.log(this.$store.state.user.userData)
      // return this.$store.getters.userData
      // return this.$store.state.user.userData
      return this.$store.state.user.userData
    },
    async profilePosts () {
      const posts = await this.$store.dispatch('profilePosts', {token: localStorage.getItem('userToken')})
      this.posts = posts
    },
  },
  methods: {
    profile () {
      if (localStorage.getItem('userToken')) {
        this.$store.dispatch('profile', {token: localStorage.getItem('userToken')})
      } else {
        this.$router.push({name: 'SignIn'})
      }
    },
    // async profilePosts () {
    //   const posts = await this.$store.dispatch('profilePosts', {token: localStorage.getItem('userToken')})
    //   this.posts = posts
    // }
  }
}
</script>

<style scoped>

</style>
