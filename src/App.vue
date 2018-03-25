<template>
  <div id="app">
    <h1>{{title}}</h1>
    <users></users>     <!-- globally & locally -->
  </div>
</template>

<script>
import Users from './Users.vue'    // locally

export default {
  components: {          // locally
    'users': Users       // locally
  },                     // locally
  data () {
    return {
      title: 'This is title'
    }
  }
}
</script>

<style>

</style>
