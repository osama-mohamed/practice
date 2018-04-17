import Vue from 'vue'
import Router from 'vue-router'
import 'vuetify/dist/vuetify.min.css'
import Home from '@/components/Home'
import CreateMeetup from '@/components/Meetup/CreateMeetup'
import Meetups from '@/components/Meetup/Meetups'
import Meetup from '@/components/Meetup/Meetup'
import Signup from '@/components/User/Signup'
import Signin from '@/components/User/Signin'
import Profile from '@/components/User/Profile'

import authGuard from './auth-guard'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/meet_up_vue',
      name: 'home',
      component: Home
    },
    {
      path: '/meet_up_vue/meetup/new',
      name: 'createmeetup',
      component: CreateMeetup,
      beforeEnter: authGuard
    },
    {
      path: '/meet_up_vue/meetups',
      name: 'meetups',
      component: Meetups
    },
    {
      path: '/meet_up_vue/meetups/:id',
      props: true,
      name: 'meetup',
      component: Meetup
    },
    {
      path: '/meet_up_vue/signup',
      name: 'signup',
      component: Signup
    },
    {
      path: '/meet_up_vue/signin',
      name: 'signin',
      component: Signin
    },
    {
      path: '/meet_up_vue/profile',
      name: 'profile',
      component: Profile,
      beforeEnter: authGuard
    }
  ]
})
