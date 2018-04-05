import Vue from 'vue'
import Router from 'vue-router'
import Articles from '@/components/Articles'
import About from '@/components/About'
import Pic from '@/components/Pic'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: __dirname,
  routes: [
    {
      path: '/',
      name: 'articles',
      component: Articles
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/pic',
      name: 'pic',
      component: Pic
    }
  ]
})
