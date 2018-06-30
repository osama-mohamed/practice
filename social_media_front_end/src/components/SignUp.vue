<template>
  <div v-if="!user">
    <h1 class="text-center">Sign Up</h1>
    <form @submit.prevent="onSubmit()">
      <div class="form-group">
        <label for="firstName">First Name</label>
        <input v-model="firstName" autocomplete="off" required type="text" class="form-control" id="firstName" aria-describedby="emailHelp" placeholder="First name">
      </div>
      <div class="form-group">
        <label for="lastName">Last Name</label>
        <input v-model="lastName" autocomplete="off" required type="text" class="form-control" id="lastName" aria-describedby="emailHelp" placeholder="Last name">
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
        <input v-model="email" autocomplete="off" required type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="E-Mail">
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
        <input v-model="password" autocomplete="off" @keyup="checkPassword()" :minlength="minlength" :maxlength="maxlength" required type="password" class="form-control" id="password" placeholder="Password">
        <small class="form-text text-muted error" v-if="password && passwordError2">Password must be more than or equal to 8 characters</small>
        <span v-if="password" v-text="password.length + ' of ' + maxlength + ' characters'"></span>
      </div>
      <div class="form-group">
        <label for="confirmPassword">Confirm Password</label>
        <input v-model="confirmPassword" autocomplete="off" @keyup="checkConfirmPassword()" :minlength="minlength" :maxlength="maxlength" required type="password" class="form-control" id="confirmPassword" placeholder="Repeat Password">
        <span v-if="confirmPassword"  v-text="confirmPassword.length + ' of ' + maxlength + ' characters'"></span>
        <small class="form-text text-muted error" v-if="confirmPassword && passwordError3">Password must be more than or equal to 8 characters</small>
        <small class="form-text text-muted error" v-if="passwordError">Passwords does not matched</small>
      </div>
      <button type="submit" class="btn btn-primary" :disabled="!formIsFilled">Sign up</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUp',
  data () {
    return {
      firstName: '',
      lastName: '',
      username: '',
      email: '',
      gender: '',
      password: '',
      confirmPassword: '',
      passwordError: false,
      passwordError2: false,
      passwordError3: false,
      genderError: false,
      available: '',
      notAvailable: '',
      notAvailableError: false,
      minlength: this.$store.state.shared.minlength,
      maxlength: this.$store.state.shared.maxlength
    }
  },
  created () {
  },
  computed: {
    user () {
      return this.$store.state.user.userData
    },
    formIsFilled () {
      this.changeGender
      return this.firstName !== ''
        && this.lastName !== ''
        && this.username !== ''
        && this.email !== ''
        && this.gender !== ''
        && this.password !== ''
        && this.confirmPassword !== ''
        && this.genderError !== true
        && this.passwordError !== true
        && this.passwordError2 !== true
        && this.passwordError3 !== true
        && this.notAvailableError !== true
    },
    formIsValid () {
      return this.password == this.confirmPassword
    },
    genderIsValid () {
      return this.gender == 'male' || this.gender == 'female'
    },
  },
  methods: {
    changeGender () {
      if (this.genderIsValid) {
        this.genderError = false
      }
    },
    checkUsernameAvailability () {
      if (this.$store.state.checkUsername === true) {
        this.available = null
        this.notAvailable = 'not available'
        this.notAvailableError = true
      } else {
        this.notAvailable = null
        this.available = 'available'
        this.notAvailableError = false
      }
    },
    async checkUsername() {
      const newUsername = await this.$store.dispatch('checkUsername', this.username)
        this.checkUsernameAvailability()
    },
    checkPassword () {
      if (!this.genderIsValid) {
        this.genderError = true
      }
      if (!this.formIsValid) {
        this.passwordError = true
      } else {
        this.passwordError = false
      }
      if (this.password.length < this.minlength) {
        this.passwordError2 = true
      } else {
        this.passwordError2 = false
      }
    },
    checkConfirmPassword () {
      if (!this.formIsValid) {
        this.passwordError = true
      } else {
        this.passwordError = false
      }
      if (this.confirmPassword.length < this.minlength) {
        this.passwordError3 = true
      } else {
        this.passwordError3 = false
      }
    },
    onSubmit () {
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

        this.firstName= ''
        this.lastName= ''
        this.username= ''
        this.email= ''
        this.gender= ''
        this.password= ''
        this.confirmPassword= ''
        this.passwordError= false
        this.passwordError2= false
        this.passwordError3= false
        this.genderError= false
        this.available= ''
        this.notAvailable= ''
        this.notAvailableError= false
        this.minlength= ''
        this.maxlength= ''
      }
    }
  }
}
</script>

<style scoped>

</style>
