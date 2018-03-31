import Vue from 'vue'
import App from './App.vue'

import VueResource from 'vue-resource'
import VueRouter from 'vue-router'
import Routes from './routes'

Vue.use(VueResource);
Vue.use(VueRouter);


const routerComponents = new VueRouter({
  routes: Routes,
  // mode: 'hash'    // default
  mode: 'history'
});

new Vue({
  el: '#app',
  render: h => h(App),
  router: routerComponents
});
