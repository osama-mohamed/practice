<template>
  <div id="app">
    <Navbar></Navbar>
    <div class="container">
      <h3 class="center-align">Developed By : <a href="https://www.facebook.com/osama.mohamed.ms">OSAMA MOHAMED</a></h3>
      <hr style="width: 70%">
      <router-view/>
    </div>
  </div>
</template>

<script>
import Navbar from './components/Navbar'

export default {
  name: 'App',
  components: {
    Navbar,
  }
}
</script>

<style>

</style>
