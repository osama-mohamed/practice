<template>
  <div id="app">
    <Navbar></Navbar>
    <div class="container">
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
input:focus{
  border-bottom: 1px solid #2196F3!important;
  -webkit-box-shadow: 0 1px 0 0 #2196F3!important;
  box-shadow: 0 1px 0 0 #2196F3!important;
}

label.active{
  color: #2196F3!important;
}
</style>
