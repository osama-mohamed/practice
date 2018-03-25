<template>
  <ul>
    <li v-for="user in users">{{user}}</li>
  </ul>
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

<style>

</style>
