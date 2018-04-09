import Vue from 'vue'
import Router from 'vue-router'
import Articles from '@/components/Articles'
import About from '@/components/About'
import Picture from '@/components/Picture'
import PictureTwo from '@/components/PictureTwo'
import PictureThree from '@/components/PictureThree'

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
      path: '/picture',
      name: 'picture',
      component: Picture
    },
    {
      path: '/pictureTwo',
      name: 'pictureTwo',
      component: PictureTwo
    },
    {
      path: '/pictureThree',
      name: 'pictureThree',
      component: PictureThree
    }
  ]
})
