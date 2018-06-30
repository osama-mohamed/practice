import Vue from 'vue'
import App from './App'
import router from './router'
import {store} from './store'
import VueResource from 'vue-resource'
import DateTimeFilter from './filters/date'

const eventBus = {}

eventBus.install = function (Vue) {
  Vue.prototype.$bus = new Vue()
}

Vue.use(eventBus)

Vue.filter('DateTime', DateTimeFilter)

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
