<template>
  <div>
    <h1 class="text-center">Sign Up</h1>
    <form @submit.prevent="onSubmit()">
      <div class="form-group">
        <label for="firstName">First Name</label>
        <input v-model="firstName" required type="text" class="form-control" id="firstName" aria-describedby="emailHelp" placeholder="First name">
      </div>
      <div class="form-group">
        <label for="lastName">Last Name</label>
        <input v-model="lastName" required type="text" class="form-control" id="lastName" aria-describedby="emailHelp" placeholder="Last name">
      </div>
      <div class="form-group">
        <label for="username">Username</label>
        <input v-model="username" required type="text" class="form-control" id="username" aria-describedby="emailHelp" placeholder="Username">
      </div>
      <div class="form-group">
        <label for="email">Email address</label>
        <input v-model="email" required type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="E-Mail">
        <small id="emailHelp" class="form-text text-muted" v-if="email">We'll never share your email with anyone else.</small>
      </div>
      <div class="form-group">
        <label for="gender">Select Gender</label>
        <select class="form-control" id="gender" v-model="gender">
          <option value="male">Male</option>
          <option value="female">Female</option>
        </select>
        <small id="emailHelp" class="form-text text-muted error" v-if="email">Please select a valid gender.</small>
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
      <button type="submit" class="btn btn-primary" >Sign up</button>
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
      username: null,
      email: null,
      gender: 'Select gender',
      password: null,
      confirmPassword: null,
      passwordError: false,
      genderError: false,
    }
  },
  computed: {
    formIsFilled () {
      return this.firstName !== null && this.lastName !== null &&  this.username !== null &&  this.email !== null && this.password !== null && this.confirmPassword !== null
    },
    formIsValid () {
      return this.password == this.confirmPassword
    },
    genderIsValid () {
      return this.gender == 'male' || this.gender == 'female'
    }
  },
  methods: {
    onSubmit () {
      if (!this.formIsValid) {
        this.passwordError = true
        return
      }
      if (!this.genderIsValid) {
        this.genderError = true
        return
      }
      let newUser = {
        firstName: this.firstName,
        lastName: this.lastName,
        username: this.username,
        email: this.email,
        gender: this.gender,
        password: this.password,
        confirmPassword: this.confirmPassword
      }
      this.$store.dispatch('SignUp', newUser)

      this.firstName= null
      this.lastName= null
      this.username= null
      this.email= null
      this.gender= null
      this.password= null
      this.confirmPassword= null
      this.passwordError= false
      this.genderError= false
    }
  }
}
</script>

<style scoped>
.error {
  color: red!important;
}
</style>
