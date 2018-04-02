import Vue from 'vue'
import Router from 'vue-router'
import Articles from '@/components/Articles'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: __dirname,
  routes: [
    {
      path: '/',
      name: 'articles',
      component: Articles
    }
  ]
})
