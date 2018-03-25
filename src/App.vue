<template>
  <div>
    <vue-header></vue-header>
    <users></users>
    <vue-footer></vue-footer>
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Users from './components/Users.vue'
import Footer from './components/Footer.vue'

export default {
  components: {
    'vue-header': Header,
    'users': Users,
    'vue-footer': Footer
  },
  data () {
    return {

    }
  }
}
</script>

<style scoped>

</style>
