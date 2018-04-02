<template>
  <div>
    <div class="container">
    <div class="row">
      <div class="col s12 m8 offset-m2">
        <div class="login card-panel blue white-text center">
          <h3>Login</h3>
          <form action="index.html">
            <div class="input-field">
              <i class="material-icons prefix white-text">email</i>
              <input type="email" id="email" v-model="email" class="white-text">
              <label class="white-text" for="email">Email Address</label>
            </div>
            <div class="input-field">
              <i class="material-icons prefix white-text">lock</i>
              <input type="password" id="password" v-model="password" class="white-text">
              <label class="white-text" for="password">Password</label>
            </div>
            <button v-on:click="login" class="btn btn-extended white black-text">Login</button>
          </form>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import firebase from 'firebase'

export default {
  name: 'login',
  data () {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    login (e) {
      firebase.auth().signInWithEmailAndPassword(this.email, this.password)
        .then(user => {
          alert(`You logged in as ${user.email}`)
          this.$router.push({name: 'dashboard'})
//          this.$router.go({path: this.$router.path})
        },
        error => {
          alert(error.message)
        })
      e.preventDefault()
    }
  }
}
</script>

<style scoped>
input,
input:focus{
  border-bottom: 1px solid #fff!important;
  -webkit-box-shadow: 0 1px 0 0 #fff!important;
  box-shadow: 0 1px 0 0 #fff!important;
}

</style>
