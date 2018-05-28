<template>
  <div>
    <h1 class="text-center">Sign Up</h1>
    <form @submit.prevent="onSubmit()">
      <div class="form-group">
        <label for="firstName">First Name</label>
        <input v-model="firstName" required type="text" class="form-control" id="firstName" aria-describedby="emailHelp" placeholder="Enter first name">
      </div>
      <div class="form-group">
        <label for="lastName">Last Name</label>
        <input v-model="lastName" required type="text" class="form-control" id="lastName" aria-describedby="emailHelp" placeholder="Enter last name">
      </div>
      <div class="form-group">
        <label for="email">Email address</label>
        <input v-model="email" required type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Enter email">
        <small id="emailHelp" class="form-text text-muted" v-if="email">We'll never share your email with anyone else.</small>
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input v-model="password" required type="password" class="form-control" id="password" placeholder="Password">
      </div>
      <div class="form-group">
        <label for="confirmPassword">Confirm Password</label>
        <input v-model="confirmPassword" required type="password" class="form-control" id="confirmPassword" placeholder="Repeat Password">
        <small id="emailHelp" class="form-text text-muted error" v-if="passwordError">Passwords does not matched</small>
      </div>
      <button type="submit" class="btn btn-primary" :disabled="!formIsFilled">Sign up</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      firstName: null,
      lastName: null,
      email: null,
      password: null,
      confirmPassword: null,
      passwordError: false
    }
  },
  computed: {
    formIsFilled () {
      return this.firstName !== null && this.lastName !== null &&  this.email !== null && this.password !== null && this.confirmPassword !== null
    },
    formIsValid () {
      return this.password == this.confirmPassword
    }
  },
  methods: {
    onSubmit () {
      if (!this.formIsValid) {
        this.passwordError = true
        return
      }
      let newUser = {
        firstName: this.firstName,
        lastName: this.lastName,
        email: this.email,
        password: this.password,
        confirmPassword: this.confirmPassword
      }
      this.$store.dispatch('SignUp', newUser)

      this.firstName= null
      this.lastName= null
      this.email= null
      this.password= null
      this.confirmPassword= null
      this.passwordError= false      
    }
  }
}
</script>

<style scoped>
.error {
  color: red!important;
}
</style>
