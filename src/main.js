import Vue from 'vue'
import App from './App.vue'

/*
import Users from './Users.vue'    // globally
Vue.component('users', Users);     // globally
*/

new Vue({
  el: '#app',
  render: h => h(App)
})
