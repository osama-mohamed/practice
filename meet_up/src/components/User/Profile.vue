<template>
  <div v-if="user">
    <v-container>
      <v-layout row wrap>
        <v-flex xs12 class="text-xs-center">
          <h1>You logged in as : {{user.email}}</h1>
          <h2>Your id is : {{user.id}}</h2>
          <ul>
            <li>you registered in : </li>
            <li v-for="meetup in user.registeredMeetups" :key="meetup">{{meetup}}</li>
          </ul>
          <br>
          <ul>
            <li>Firebase keys is : </li>
            <li v-for="fbkey in user.fbkeys" :key="fbkey">{{fbkey}}</li>
          </ul>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
export default {
  computed: {
    user () {
      return this.$store.getters.user
    }
  }
}
</script>

<style scoped>
</style>
