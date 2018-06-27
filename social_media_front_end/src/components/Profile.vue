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
    this.getUser()
    },
  computed: {
    user () {
      return this.$store.state.user.userData
    }
  },
  methods: {
    getUser () {
      // this.$store.dispatch('getUser', {id: sessionStorage.getItem('userID')})
      this.$store.dispatch('getUser', {token: sessionStorage.getItem('userToken')})
    }
  }
}
</script>

<style scoped>

</style>
