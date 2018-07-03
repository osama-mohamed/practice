<template>
  <div v-if="user">
    <div>
      <h1 class="text-center">Profile</h1>
      <h2 class="text-center">{{username}}</h2>

      <div class="container">
        <div class="row">
          <div v-for="post in posts" :key="post.id" class="card col-sm-6 offset-sm-3 my-2">
            <div>
              <img class="mr-2 mt-4" style="border-radius: 50%; width: 40px; height: 40px;" v-if="post.image" :src="'/static/uploads/' + post.image" :alt="post.post">
              <span style="top: 3px; position: relative; font-size: 14px; font-weight: 600; color: #365899;">{{username}}</span>
              <span style="position: absolute; top: 46px; left: 69px; font-size: 12px;">{{post.added | DateTime}}</span>
            </div>
            <div class="">
              <button class="menu-button" style="position: relative; left: 496px; top: -50px; cursor: pointer; font-weight: 900; background: none; border: none;" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                ...
              </button>
              <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <a class="dropdown-item" href="#">Edit Post</a>
                <a class="dropdown-item" href="#">Delete</a>
              </div>
            </div>
            <p class="card-text mt-1">{{post.post}}</p>
            <div class="mb-3">
              <a :href="'/static/uploads/' + post.image" target="_blank" class="mt-4">
                <img class="card-img-top" v-if="post.image" :src="'/static/uploads/' + post.image" :alt="post.post">
              </a>
            </div>
            <div class="mb-3">
              <form class="form-group">
                <img class="mr-2 mt-4" style="border-radius: 50%; width: 40px; height: 40px;" v-if="post.image" :src="'/static/uploads/' + post.image" :alt="post.post">
                <textarea type="text" class="form-control" placeholder="Write a comment ..." style="position: relative; top: -35px; left: 48px; max-width: 90%; border-radius: 20px; overflow: hidden; height: 38px; min-height: 38px;"></textarea>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'

export default {
  name: 'Profile',
  data () {
    return {
      posts: [],
      username: null
    }
  },
  beforeRouteEnter (from, to, next) {
    Vue.http.post(`http://localhost:8000/api/posts/profile_posts_for_username/`, {username: from.params.username})
      .then(data => {
        next(vm=>{
        vm.posts = data.body.user.posts
        vm.username = data.body.user.username
        })
        return data.body.user.posts
      })
      .catch(error => {
        console.log(error)
      })
  },
  created() {
    // this.profile()
    // this.profilePosts
  },
  computed: {
    user () {
      // console.log(this.$store.getters.userData)
      // console.log(this.$store.state.user.userData)
      // return this.$store.getters.userData
      // return this.$store.state.user.userData
      return this.$store.state.user.userData
    },
  },
  methods: {
    // profile () {
    //   if (localStorage.getItem('userToken')) {
    //     this.$store.dispatch('profile', {token: localStorage.getItem('userToken')})
    //   } else {
    //     this.$router.push({name: 'SignIn'})
    //   }
    // },
    // async profilePosts () {
    //   const posts = await this.$store.dispatch('profilePosts', {token: localStorage.getItem('userToken')})
    //   this.posts = posts
    // }
  }
}
</script>

<style scoped>
.dropdown-menu.show {
  left: -136px !important;
}
.menu-button {
  outline: none !important;
}
</style>
