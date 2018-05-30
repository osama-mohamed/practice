import Vue from 'vue'
import Router from 'vue-router'
import SignUp from '@/components/SignUp'
import SignIn from '@/components/SignIn'
import HomePage from '@/components/HomePage'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/signup',
      name: 'SignUp',
      component: SignUp
    },
    {
      path: '/signin',
      name: 'SignIn',
      component: SignIn
    },
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
  ]
})
