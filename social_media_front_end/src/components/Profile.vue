<template>
  <div v-if="user">
    <div>
      <h1 class="text-center">Profile</h1>
      <h2 class="text-center">{{username}}</h2>
      <div v-if="alertMessage" class="alert alert-success alert-dismissible fade show" role="alert" style="margin: auto; max-width: 50%;">
        {{alertMessage}}
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>

      <div class="container">
        <div class="row">
          <div v-for="post in posts" :key="post.id" :data-id="post.id" class="card col-sm-6 offset-sm-3 my-2">
            <div>
              <img class="mr-2 mt-4" style="border-radius: 50%; width: 40px; height: 40px;" v-if="userProfilePic" :src="'/static/uploads/' + userProfilePic" :alt="post.post">
              <span style="top: 3px; position: relative; font-size: 14px; font-weight: 600; color: #365899;">{{username}}</span>
              <span style="position: absolute; top: 46px; left: 69px; font-size: 12px;">{{post.added | DateTime}}</span>
            </div>
            <div class="">
              <button class="menu-button" style="position: relative; left: 496px; top: -50px; cursor: pointer; font-weight: 900; background: none; border: none;" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                ...
              </button>
              <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <a class="dropdown-item" href="#">Edit Post</a>
                <a class="dropdown-item" href="#" @click.prevent="deletePost">Delete</a>
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
                <img class="mr-2 mt-4" style="border-radius: 50%; width: 40px; height: 40px;" v-if="userProfilePic" :src="'/static/uploads/' + userProfilePic" :alt="post.post">
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
      username: null,
      userProfilePic: null,
      alertMessage: null,
    }
  },
  beforeRouteEnter (from, to, next) {
    next(vm => {
      vm.$store.dispatch('ProfilePostsForUsername', {username: from.params.username})
        .then(data => {
          vm.posts = data.posts
          vm.username = data.username
          vm.userProfilePic = data.userProfilePic
        })
        .catch(error => {
          console.log(error)
        })
    })
  },
  // beforeCreate () {
  //   this.$store.dispatch('ProfilePostsForUsername', {username: this.$route.params.username})
  //     .then(data => {
  //       console.log(data)
  //       this.posts = data.posts
  //       this.username = data.username
  //       this.userProfilePic = data.userProfilePic
  //     })
  //     .catch(error => {
  //       console.log(error)
  //     })
  // },
  created() {
    // this.post()
  },
  computed: {
    user () {
      return this.$store.state.user.userData
    },
  },
  // watch: {
  //   '$route': 'post',
  //   '$route': 'beforeRouteEnter'
  // },
  methods: {
    // async post () {
    //   await this.$store.dispatch('ProfilePostsForUsername', {username: this.$route.params.username})
    //     .then(data => {
    //       console.log(data)
    //       this.posts = data.posts
    //       this.username = data.username
    //       this.userProfilePic = data.userProfilePic
    //     })
    //     .catch(error => {
    //       console.log(error)
    //     })
    // },
    async deletePost (e) {
      const deletePostData = await this.$store.dispatch('deleteProfilePost', {id: e.path[3].dataset.id})
      this.alertMessage = deletePostData.body.message.message
      setTimeout(() => {
        this.alertMessage = null
      }, 3000)
      e.path[3].remove()
    }
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
