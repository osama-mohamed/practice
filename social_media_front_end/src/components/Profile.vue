<template>
  <div v-if="user">
    <div>
      <h1 class="text-center">Profile</h1>
      <h2 class="text-center">{{user}}</h2>

      <div class="container">
        <div class="row">
          <div v-for="post in posts" :key="post.id" class="card col-sm-6 offset-sm-3 my-2" style="width: 49%;">
            <div>
              <img class="mr-2 mt-4" style="border-radius: 50%; max-width: 40px;" v-if="post.image" :src="'static/uploads/' + post.image" :alt="post.post">
              <span style="top: 2px; position: relative; font-size: 18px; font-weight: bold; color: #365899;">{{user.username}}</span>
              <!-- <span style="position: relative; top: 14px; left: -14px;">{{post.added | DateTime}}</span> -->
              <span style="position: absolute; top: 44px; left: 69px; font-size: 12px;">{{post.added | DateTime}}</span>
            </div>
            <div class="dropdown show">
              <a style="position: relative; left: 496px; top: -54px; cursor: pointer; font-weight: 900;" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                ...
              </a>
              <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <a class="dropdown-item" href="#">Edit Post</a>
                <a class="dropdown-item" href="#">Delete</a>
              </div>
            </div>
            <a :href="'static/uploads/' + post.image" target="_blank" class="mt-4">
              <img class="card-img-top" v-if="post.image" :src="'static/uploads/' + post.image" :alt="post.post">
            </a>
            <div class="card-body">
              <!-- <img class="card-img-top mr-2" style="border-radius: 50%; max-width: 40px;" v-if="post.image" :src="'static/uploads/' + post.image" :alt="post.post">
              <span style="top: -8px; position: relative; font-size: 18px; font-weight: bold; color: #365899;">{{user.username}}</span> -->
              <!-- <span style="position: relative; top: 14px; left: -14px;">{{post.added | DateTime}}</span> -->
              <!-- <span style="position: absolute; bottom: 130px; left: 87px; font-size: 12px;">{{post.added | DateTime}}</span> -->
              <p class="card-text">{{post.post}}</p>
              <h5 class="card-title">#{{post.id}}</h5>
              <h5 class="card-title">{{post.updated | DateTime}}</h5>
              <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
            </div>
          </div>
        </div>
      </div>
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
.dropdown-menu.show {
  left: -142px !important;
}
</style>
