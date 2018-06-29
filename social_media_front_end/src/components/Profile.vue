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
      return this.$store.state.user.userData
    }
  },
  methods: {
    profile () {
      if (sessionStorage.getItem('userToken')) {
        this.$store.dispatch('profile', {token: sessionStorage.getItem('userToken')})
      } else {
        this.$router.push({name: 'SignIn'})
      }
    }
  }
}
</script>

<style scoped>

</style>
