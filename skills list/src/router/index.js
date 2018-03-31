import Vue from 'vue'
import Router from 'vue-router'
import Skills from '@/components/Skills'
import About from '@/components/About'

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: __dirname,
  routes: [
    {
      path: '/',
      name: 'Skills',
      component: Skills
    },
    {
      path: '/about/:name',
      name: 'About',
      component: About
    }
  ]
})
