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
        <input v-model="username" @keyup="checkUsername()" autocomplete="off" required type="text" class="form-control" id="username" aria-describedby="emailHelp" placeholder="Username">
        <small class="form-text text-muted success" v-if="username && available">{{username}} is {{available}}</small>
        <small class="form-text text-muted error" v-if="username && notAvailable">{{username}} is {{notAvailable}}</small>
        <small class="form-text text-muted error" v-if="notAvailableError && notAvailable">This {{username}} is {{notAvailable}}, so please select another username</small>
      </div>
      <div class="form-group">
        <label for="email">Email address</label>
        <input v-model="email" required type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="E-Mail">
        <small class="form-text text-muted" v-if="email">We'll never share your email with anyone else.</small>
      </div>
      <div class="form-group">
        <label for="gender">Select Gender</label>
        <select class="form-control" id="gender" v-model="gender" @change="changeGender()">
          <option value="male">Male</option>
          <option value="female">Female</option>
        </select>
        <small class="form-text text-muted error" v-if="genderError">Please select a valid gender.</small>
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input v-model="password" required type="password" class="form-control" id="password" placeholder="Password">
      </div>
      <div class="form-group">
        <label for="confirmPassword">Confirm Password</label>
        <input v-model="confirmPassword" required type="password" class="form-control" id="confirmPassword" placeholder="Repeat Password">
        <small class="form-text text-muted error" v-if="passwordError">Passwords does not matched</small>
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
      available: null,
      notAvailable: null,
      notAvailableError: false
    }
  },
  created () {
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
    changeGender () {
      if (this.gender == null) {
        this.genderError = true
      }
      if (this.gender == 'male' || this.gender == 'female') {
        this.genderError = false
      }
    },
    checkUsernameAvailability () {
      if (this.$store.state.checkUsername === true) {
        this.available = null
        this.notAvailable = 'not available'
      } else {
        this.notAvailable = null
        this.available = 'available'
      }
    },
    checkUsername() {
      this.$store.dispatch('checkUsername', this.username)
      setTimeout (() => {
        this.checkUsernameAvailability()
      }, 600)
    },
    onSubmit () {
      if (!this.formIsValid) {
        this.passwordError = true
        return
      }
      if (!this.genderIsValid) {
        this.genderError = true
        return
      }
      if (this.notAvailable) {
        this.notAvailableError = true
        return
      }
      if (!this.notAvailable) {
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
        this.$router.push({name: 'SignIn'})

        this.firstName= null
        this.lastName= null
        this.username= null
        this.email= null
        this.gender= null
        this.password= null
        this.confirmPassword= null
        this.passwordError= false
        this.genderError= false
        this.available= null
        this.notAvailable= null
        this.notAvailableError= false
      }
    }
  }
}
</script>

<style scoped>

</style>
