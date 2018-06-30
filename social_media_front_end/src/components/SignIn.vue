<template>
  <div v-if="!user">
    <h1 class="text-center">Sign In</h1>
    <div class="alert alert-danger alert-dismissible fade show" role="alert" v-if="signInError && signInErrorMessage">
      {{signInErrorMessage}}
      <button type="button" class="close" data-dismiss="alert" aria-label="Close">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    <form @submit.prevent="onSubmit()">
      <div class="form-group">
        <label for="username">Username</label>
        <input v-model="username" autocomplete="off" required type="text" class="form-control" id="username" aria-describedby="emailHelp" placeholder="Username">
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input v-model="password" autocomplete="off" required type="password" class="form-control" id="password" placeholder="Password">
      </div>
      <button type="submit" class="btn btn-primary" >Sign in</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignIn',
  data () {
    return {
      username: null,
      password: null,
      signInError: false,
      signInErrorMessage: null
    }
  },
  computed: {
    user () {
      return this.$store.state.user.userData
    }
  },
  methods: {
    checkSignIn () {
      if (this.$store.state.signInError === true) {
        this.signInError = false
        this.signInErrorMessage = null
      } else {
        this.signInError = true
        this.signInErrorMessage = this.$store.state.signInErrorMessage
      }
    },
    async onSubmit () {
      let user = {
        username: this.username,
        password: this.password
      }
      const userStatus = await this.$store.dispatch('SignIn', user)
      this.checkSignIn()
      if (this.signInError === false) {
        this.$router.push({name: 'Profile'})
        this.username= null
        this.password= null
        this.passwordError= false
        this.signInError = false
      }
    }
  }
}
</script>

<style scoped>

</style>
