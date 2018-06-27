<template>
  <div id="app" class="container">
    <NavBar/>
    <router-view/>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar'

export default {
  name: 'App',
  components: {
    NavBar
  }
}
</script>

<style>
/* npm i prettier@~1.12.0 */
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  box-sizing: border-box;
}
.error {
  color: red!important;
}
.success {
  color: green!important;
}
</style>