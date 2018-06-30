import Vue from 'vue'

export default {
  state: {
  },
  mutations: {
  },
  actions: {
      newPost ({commit}, payload) {
        Vue.http.post(`${this.state.shared.baseURL}posts/new_post/`, payload, {
          progress: uploadEvent => {
            console.log('Upload Progress : ' + Math.round((uploadEvent.loaded / uploadEvent.total) * 100) + ' %')
          }
        }
      )
        .then(data => {
        })
        .catch(error => {
          console.log(error)
        })
      },
  },
  getters: {
    
  }
}