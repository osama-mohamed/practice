import Vue from 'vue'
import Router from 'vue-router'
import SignUp from '@/components/SignUp'
import SignIn from '@/components/SignIn'
import HomePage from '@/components/HomePage'
import Profile from '@/components/Profile'
// import Profile2 from '@/components/Profile2'
import NewPost from '@/components/NewPost'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/sign-up',
      name: 'SignUp',
      component: SignUp
    },
    {
      path: '/sign-in',
      name: 'SignIn',
      component: SignIn
    },
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    // {
    //   path: '/profile',
    //   name: 'Profile',
    //   component: Profile
    // },
    {
      path: '/new-post',
      name: 'NewPost',
      component: NewPost
    },
    {
      path: '/profile/:username',
      name: 'Profile',
      component: Profile
    },
  ]
})
