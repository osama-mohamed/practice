import Vue from 'vue'
import App from './App'
import router from './router'
import {store} from './store'
import VueResource from 'vue-resource'


Vue.config.productionTip = false
Vue.use(VueResource)


new Vue({
  el: '#app',
  router,
  store,
  VueResource,
  components: { App },
  template: '<App/>'
})
