import Vue from 'vue'
import Router from 'vue-router'
import Calculator from '@/components/Calculator'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: __dirname,
  routes: [
    {
      path: '/mac_calculator_vue/',
      name: 'Calculator',
      component: Calculator
    }
  ]
})
