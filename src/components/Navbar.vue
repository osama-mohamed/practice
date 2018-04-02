<template>
  <nav>
    <div class="nav-wrapper blue">
      <div class="container">
        <router-link v-bind:to="{name: 'dashboard'}" class="brand-logo">Employee Manager</router-link>
        <ul class="right">
          <li v-if="isLoggedIn"><span class="email white-text">{{currentUser}}</span></li>
          <li v-if="isLoggedIn"><router-link v-bind:to="{name: 'dashboard'}">Dashboard</router-link></li>
          <li v-if="!isLoggedIn"><router-link v-bind:to="{name: 'login'}">Login</router-link></li>
          <li v-if="!isLoggedIn"><router-link v-bind:to="{name: 'register'}">Register</router-link></li>
          <li v-if="isLoggedIn"><button v-on:click="logout" class="btn black">Logout</button></li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import firebase from 'firebase'

export default {
  name: 'navbar',
  data () {
    return {
      isLoggedIn: false,
      currentUser: false
    }
  },
  created () {
    this.changeNavbar()

//    firebase.auth().onAuthStateChanged(function(user) {
//      if (user) {
//        this.isLoggedIn = true
//        this.currentUser = firebase.auth().currentUser.email
//        // User is signed in.
//        console.log('logged')
//      }
//      else {
//        this.isLoggedIn = false
//        this.currentUser = false
//        // No user is signed in.
//        console.log('out')
//      }
//    });

  },
  watch: {
    '$route': 'changeNavbar'
  },
  methods: {
    changeNavbar() {
      if (firebase.auth().currentUser) {
        this.isLoggedIn = true
        this.currentUser = firebase.auth().currentUser.email
      } else {
        this.isLoggedIn = false
        this.currentUser = false
      }
    },
    logout () {
      firebase.auth().signOut()
        .then(() => {
          this.$router.push({name: 'login'})
          this.changeNavbar()
//          this.$router.go({path: this.$router.path})
        })
    }

  }
}
</script>

<style scoped>
.email{
  padding-right: 12px;
}
</style>
