import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '@/components/Dashboard'
import NewEmployee from '@/components/NewEmployee'
import ViewEmployee from '@/components/ViewEmployee'
import EditEmployee from '@/components/EditEmployee'
import Login from '@/components/Login'
import Register from '@/components/Register'
import firebase from 'firebase'


Vue.use(Router)

let router = new Router({
  mode: 'history',
  base: __dirname,
  routes: [
    {
      path: '/employee_manager_vue',
      name: 'dashboard',
      component: Dashboard,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/employee_manager_vue/login',
      name: 'login',
      component: Login,
      meta: {
        requiresGuest: true,
      }
    },
    {
      path: '/employee_manager_vue/register',
      name: 'register',
      component: Register,
      meta: {
        requiresGuest: true,
      }
    },
    {
      path: '/employee_manager_vue/new',
      name: 'new-employee',
      component: NewEmployee,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/employee_manager_vue/edit/:employee_id',
      name: 'edit-employee',
      component: EditEmployee,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/employee_manager_vue/:employee_id',
      name: 'view-employee',
      component: ViewEmployee,
      meta: {
        requiresAuth: true,
      }
    },
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!firebase.auth().currentUser) {
      next({
        name: 'login',
        query: {
          redirect: to.fullPath
        }
      })
    } else {
      next()
    }
  } else if (to.matched.some(record => record.meta.requiresGuest)) {
    if (firebase.auth().currentUser) {
      next({
        name: 'dashboard',
        query: {
          redirect: to.fullPath
        }
      })
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
