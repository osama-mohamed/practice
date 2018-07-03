<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <router-link class="navbar-brand" :to="{name: 'HomePage'}">Social Media</router-link>
    <router-link class="navbar-brand" :to="{name: 'HomePage'}">{{username}}</router-link>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link class="nav-link" :to="{name: 'HomePage'}">Home</router-link>
        </li>
        <li class="nav-item" v-if="!user">
          <router-link class="nav-link" :to="{name: 'SignUp'}">Sign Up</router-link>
        </li>
        <li class="nav-item" v-if="!user">
          <router-link class="nav-link" :to="{name: 'SignIn'}">Sign In</router-link>
        </li>
        <li class="nav-item" v-if="user">
          <router-link class="nav-link" :to="{name: 'Profile'}">Profile</router-link>
        </li>
        <li class="nav-item" v-if="user">
          <router-link class="nav-link" :to="{name: 'NewPost'}">New Post</router-link>
        </li>



        <!-- <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Settings
          </a>
          <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <router-link class="dropdown-item" to="/">Action</router-link>
            <router-link class="dropdown-item" href="#">Another action</router-link>
            <div class="dropdown-divider"></div>
            <router-link class="dropdown-item" href="#">Something else here</router-link>
          </div>
        </li> -->


        <!-- <li class="nav-item">
          <a class="nav-link disabled" href="#">Disabled</a>
        </li> -->


      <!--
      <ul class="navbar-nav mr-auto">
        <li class="nav-item" v-if="user">
          <button class="btn btn-link" @click="signOut()">Sign Out</button>
        </li> 
      </ul>
        -->
      </ul>

        
        <div class="btn-group">
          <button type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Action
          </button>
          <div class="dropdown-menu">
            <a href="" class="dropdown-item" @click.prevent="changeProfilePic()">Change Profile Pic</a>
            <!-- <a href="" class="dropdown-item">Profile</a>
            <a href="" class="dropdown-item">Update Profile</a>
            <a href="" class="dropdown-item">Change Password</a> -->
            <div class="dropdown-divider"></div>
            <a href="" class="dropdown-item" @click.prevent="signOut()">Sign Out</a>
          </div>
        </div>
        <input type="file" ref="profilePic" style="display: none;" v-on:change="fileChange($event.target.files)">


      <!-- <form class="form-inline my-2 my-lg-0">
        <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
      </form> -->
    </div>
  </nav>
</template>


<script>
export default {
  name: 'NavBar',
  data () {
    return {
      username: null,
      image: null
    }
  },
  computed: {
    user () {
      return this.$store.state.user.userData
    },
  },
  methods: {
    async signOut () {
      if (localStorage.getItem('userToken')) {
        const logOutUser = await this.$store.dispatch('SignOut', {token: localStorage.getItem('userToken')})
        localStorage.removeItem('userToken')
        this.$router.push({name: 'HomePage'})
      }
    },
    async fileChange(fileList) {
      this.image = fileList[0]
      const profilePic = new FormData()
      profilePic.append('token', localStorage.getItem('userToken'))
      profilePic.append('file', this.image, this.image.name)
      
      const u = await this.$store.dispatch('profilePic', profilePic)
      // console.log(u)
      // console.log(this.username)
      this.$store.dispatch('ProfilePostsForUsername', {username: 'OSAMA.MOHAMED'})
      this.$refs.profilePic.type = 'text'
      this.$refs.profilePic.type = 'file'
    },
    changeProfilePic () {
      this.$refs.profilePic.click()
    }
  }
}
</script>

<style scoped>

</style>