import Vue from 'vue'
import Router from 'vue-router'
import TranslateForm from '@/components/TranslateForm'

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: __dirname,
  routes: [
    {
      path: '/',
      name: 'TranslateForm',
      component: TranslateForm
    }
  ]
})
