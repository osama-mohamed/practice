<template>
  <header>
    <h1 v-on:click="changeTitle">{{title}}</h1>
  </header>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
    }
  },
  data () {
    return {
      title: 'Vue header'
    }
  },
  methods: {
    changeTitle: function () {
      this.title = 'This is another title'
    }
  }
}
</script>

<style scoped>
header{
    background: lightgreen;
    padding: 10px;
}
h1{
    color: #222;
    text-align: center;
}
</style>
