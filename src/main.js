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

Vue.config.productionTip = false
Vue.use(Vuetify)

Vue.filter('DateTime', DateTimeFilter)
Vue.component('app-alert', Alert)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
  created () {
    firebase.initializeApp({
      apiKey: 'AIzaSyCa9N5ha0wSBKDBdEwyndU5q_jxq5vsIUQ',
      authDomain: 'meetups-vue.firebaseapp.com',
      databaseURL: 'https://meetups-vue.firebaseio.com',
      projectId: 'meetups-vue',
      storageBucket: ''
    })
  }
})

Vue.use(Vuetify, {
  theme: {
    primary: colors.red.darken1, // #E53935
    secondary: colors.red.lighten4, // #FFCDD2
    accent: colors.indigo.base // #3F51B5
  }
})
