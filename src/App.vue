<template>
  <div>
    <vue-header v-bind:title="title"></vue-header>
    <users v-bind:users="usersInfo"></users>
    <vue-footer v-bind:title="title"></vue-footer>
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
      usersInfo:[
        {name: 'Osama', speciality: 'Vue Components', show: false},
        {name: 'Mohamed', speciality: 'HTML Wizardry', show: false},
        {name: 'Mahmoud', speciality: 'Click Events', show: false},
        {name: 'Ahmed', speciality: 'Conditionals', show: false},
        {name: 'Eslam', speciality: 'Webpack', show: false},
        {name: 'Nasser', speciality: 'Data Diggin', show: false}
      ],
      title: 'vue app new title'
    }
  }
}
</script>

<style scoped>

</style>
