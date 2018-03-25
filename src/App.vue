<template>
  <div id="app">
    <h1>{{title}}</h1>
    <p>{{greeting()}}</p>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      title: 'This is title'
    }
  },
  methods: {
    greeting: function () {
       return 'Hello Visitor'
    }
  }
}
</script>

<style>

</style>
