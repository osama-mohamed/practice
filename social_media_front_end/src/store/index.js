import Vue from 'vue'
import Vuex from 'vuex'
import user from './user'
import posts from './posts'
import shared from './shared'

Vue.use(Vuex)

export const store = new Vuex.Store({
  modules: {
    user: user,
    posts: posts,
    shared: shared
  }
})