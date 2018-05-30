<template>
  <div>
    <h1 class="text-center">Sign In</h1>
    <form @submit.prevent="onSubmit()">
      <div class="form-group">
        <label for="username">Username</label>
        <input v-model="username" autocomplete="off" required type="text" class="form-control" id="username" aria-describedby="emailHelp" placeholder="Username">
        <small class="form-text text-muted error" v-if="signInError">Username or password is invalid.</small>
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
      signInError: false
    }
  },
  computed: {
  },
  methods: {
    checkSignIn () {
      console.log(this.$store.state.signInError)
      if (this.$store.state.signInError === true) {
        this.signInError = false
      } else {
        this.signInError = true
      }
    },
    onSubmit () {
      let user = {
        username: this.username,
        password: this.password
      }
      this.$store.dispatch('SignIn', user)
      setTimeout (() => {
        this.checkSignIn()
        if (this.signInError === false) {
          this.$router.push({name: 'HomePage'})
          this.username= null
          this.password= null
          this.passwordError= false
          this.signInError = false
        }
      }, 600)
    }
  }
}
</script>

<style scoped>

</style>
