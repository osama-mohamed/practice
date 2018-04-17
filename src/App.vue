<template>
  <!--<div id="app">-->
    <v-app> <!-- dark -->
      <v-navigation-drawer temporary v-model="sideNav" app>
        <v-list>
          <v-list-tile v-for="item in menuItems" :key="item.title" :to="item.link">
            <v-list-tile-action>
              <v-icon left>{{item.icon}}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>{{item.title}}</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>

          <v-list-tile v-if="userIsAuthenticated" @click="onLogout">
            <v-list-tile-action>
              <v-icon>exit_to_app</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Logout</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-navigation-drawer>

      <v-toolbar dark class="blue">
        <v-toolbar-side-icon
          @click.stop="sideNav= !sideNav"
          class="hidden-sm-and-up"></v-toolbar-side-icon>
        <v-toolbar-title><router-link to="/" tag="span" style="cursor: pointer">Meetup</router-link></v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items class="hidden-xs-only">
          <v-btn flat v-for="item in menuItems" :key="item.title" :to="item.link">
            <v-icon left>{{item.icon}}</v-icon>
            {{item.title}}
          </v-btn>

          <v-btn flat v-if="userIsAuthenticated" @click="onLogout">
            <v-icon left>exit_to_app</v-icon>
            Logout
          </v-btn>
        </v-toolbar-items>
      </v-toolbar>
      <main>
        <h1 class="text-xs-center">Developed By : <a href="https://www.facebook.com/osama.mohamed.ms">OSAMA MOHAMED</a></h1>
        <hr style="width: 70%; margin: 0 auto;">
        <router-view/>
      </main>
    </v-app>
  <!--</div>-->
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      sideNav: false
    }
  },
  computed: {
    menuItems () {
      let menuItems = [
        {icon: 'face', title: 'Sign Up', link: '/signup'},
        {icon: 'lock_open', title: 'Sign In', link: '/signin'}
      ]
      if (this.userIsAuthenticated) {
        menuItems = [
          {icon: 'supervisor_account', title: 'View Meetups', link: '/meetups'},
          {icon: 'room', title: 'Organize Meetup', link: '/meetup/new'},
          {icon: 'person', title: 'Profile', link: '/profile'}
        ]
      }
      return menuItems
    },
    userIsAuthenticated () {
      return this.$store.getters.user !== null && this.$store.getters.user !== undefined
    }
  },
  methods: {
    onLogout () {
      this.$store.dispatch('logout')
      this.$router.push({name: 'home'})
    }
  }
}
</script>

<style>
/*@import '~vuetify/src/stylus/main.styl';*/

</style>
