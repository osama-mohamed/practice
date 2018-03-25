<template>
  <div>
    <h1>Users</h1>
    <ul>
      <li v-for="user in users">{{user}}</li>
    </ul>
  </div>
</template>

<script>
export default {
  data () {
    return {
      users: ['OSAMA', 'MOHAMED', 'MAHMOUD']
    }
  }
}
</script>

<style scoped>
h1{
  color: blue;
}
</style>
