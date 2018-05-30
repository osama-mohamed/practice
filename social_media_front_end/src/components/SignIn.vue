<template>
  <div>
    <h1 class="text-center">Sign In</h1>
    <form @submit.prevent="onSubmit()">
      <div class="form-group">
        <label for="username">Username</label>
        <input v-model="username" required type="text" class="form-control" id="username" aria-describedby="emailHelp" placeholder="Username">
      </div>
      <!-- <div class="form-group">
        <label for="email">Email address</label>
        <input v-model="email" required type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="E-Mail">
        <small id="emailHelp" class="form-text text-muted" v-if="email">We'll never share your email with anyone else.</small>
      </div> -->
      <div class="form-group">
        <label for="password">Password</label>
        <input v-model="password" required type="password" class="form-control" id="password" placeholder="Password">
      </div>
      <button type="submit" class="btn btn-primary" >Sign in</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      username: null,
      email: null,
      password: null,
    }
  },
  computed: {
  },
  methods: {
    onSubmit () {
      let user = {
        username: this.username,
        email: this.email,
        password: this.password
      }
      this.$store.dispatch('SignIn', user)

      this.username= null
      this.email= null
      this.password= null
      this.passwordError= false
    }
  }
}
</script>

<style scoped>

</style>
