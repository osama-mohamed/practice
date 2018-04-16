// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import * as firebase from 'firebase'
import Vuetify from 'vuetify'
import colors from 'vuetify/es5/util/colors'
import {store} from './store'
import DateTimeFilter from './filters/date'
import Alert from './components/Shared/Alert'
import EditMeetup from './components/Meetup/Edit/EditMeetup'
import EditMeetupDate from './components/Meetup/Edit/EditDate'
import EditMeetupTime from './components/Meetup/Edit/EditTime'
import Registration from './components/Meetup/Registration/Register'

Vue.config.productionTip = false
Vue.use(Vuetify)

Vue.filter('DateTime', DateTimeFilter)
Vue.component('app-alert', Alert)
Vue.component('app-edit-meetup', EditMeetup)
Vue.component('app-edit-meetup-date', EditMeetupDate)
Vue.component('app-edit-meetup-time', EditMeetupTime)
Vue.component('app-register', Registration)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
  created () {
    firebase.initializeApp({
      apiKey: 'AIzaSyDEuq2RgRCh2YT6V6ZarWA9VpPDcr8ytBw',
      authDomain: 'vue-meetups-app.firebaseapp.com',
      databaseURL: 'https://vue-meetups-app.firebaseio.com',
      projectId: 'vue-meetups-app',
      storageBucket: 'gs://vue-meetups-app.appspot.com',
      messagingSenderId: '209520977841'
    })
    firebase.auth().onAuthStateChanged((user) => {
      if (user) {
        this.$store.dispatch('autoSignIn', user)
        this.$store.dispatch('fetchUserMeetups')
      }
    })
    this.$store.dispatch('loadMeetups')
  }
})

Vue.use(Vuetify, {
  theme: {
    primary: colors.red.darken1, // #E53935
    secondary: colors.red.lighten4, // #FFCDD2
    accent: colors.indigo.base // #3F51B5
  }
})
