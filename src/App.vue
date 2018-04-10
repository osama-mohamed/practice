<template>
  <div id="app">
    <v-app> <!-- dark -->
      <v-toolbar>
        <v-toolbar-title>Meetup</v-toolbar-title>
        <v-toolbar-items>
          <v-btn flat>view meet up</v-btn>
        </v-toolbar-items>
      </v-toolbar>
      <router-view/>
    </v-app>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
/*@import '~vuetify/src/stylus/main'*/

</style>
