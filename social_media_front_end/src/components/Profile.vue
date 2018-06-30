<template>
  <div>
    <div v-if="user">
      <h1 class="text-center">Profile {{user}}</h1>
    </div>
    <div v-if="!user">
    </div>
  </div>
</template>

<script>
export default {
  name: 'Profile',
  data () {
    return {
    }
  },
  created() {
    this.profile()
    },
  computed: {
    user () {
      // console.log(this.$store.getters.userData)
      // console.log(this.$store.state.user.userData)
      // return this.$store.getters.userData
      // return this.$store.state.user.userData
      return this.$store.state.user.userData
    }
  },
  methods: {
    profile () {
      if (localStorage.getItem('userToken')) {
        this.$store.dispatch('profile', {token: localStorage.getItem('userToken')})
      } else {
        this.$router.push({name: 'SignIn'})
      }
    }
  }
}
</script>

<style scoped>

</style>
