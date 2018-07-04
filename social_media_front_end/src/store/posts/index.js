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
      profilePosts ({commit}, payload) {
        return Vue.http.post(`${this.state.shared.baseURL}posts/profile_posts/`, payload)
        .then(data => {
          return data.body.user.posts
        })
        .catch(error => {
          console.log(error)
        })
      },
      ProfilePostsForUsername ({commit}, payload) {
        return Vue.http.post(`${this.state.shared.baseURL}posts/profile_posts_for_username/`, payload)
        .then(data => {
          return data.body.user
        })
        .catch(error => {
          console.log(error)
        })
      },
      deleteProfilePost ({commit}, payload) {
        return Vue.http.post(`${this.state.shared.baseURL}posts/delete_profile_post/`, payload)
        .then(data => {
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