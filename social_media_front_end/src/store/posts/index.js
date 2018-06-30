import Vue from 'vue'

export default {
  state: {
  },
  mutations: {
  },
  actions: {
      newPost ({commit}, payload) {
        Vue.http.post(`${this.state.shared.baseURL}posts/new_post/`, payload)
        .then(data => {
          console.log(data)
          return data
        })
        .catch(error => {
          console.log(error)
        })
      },
  },
  getters: {
    
  }
}