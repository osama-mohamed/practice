import Vue from 'vue'

export default {
  state: {
    checkUsername: null,
    signInError: null,
    signInErrorMessage: null
  },
  mutations: {
    
  },
  actions: {
    checkUsername ({commit}, payload) {
      let newPayload = {
        username: payload
      }
      Vue.http.post(`${this.state.shared.baseURL}accounts/checkusername/`, newPayload)
        .then(data => {
          this.state.checkUsername = data.body.message.success
          return data
        })
        .catch(error => {
          console.log(error)
        })
    },
    SignUp ({commit}, payload) {
      Vue.http.post(`${this.state.shared.baseURL}accounts/signup/`, payload)
        .then(data => {
          return data
        })
        .catch(error => {
          console.log(error)
        })
        
      },
      SignIn ({commit}, payload) {
        Vue.http.post(`${this.state.shared.baseURL}accounts/signin/`, payload)
        .then(data => {
          this.state.signInError = data.body.message.success
          this.state.signInErrorMessage = data.body.message.message
          return data
        })
        .catch(error => {
          console.log(error)
        })
        
    }
  },
  getters: {
    
  }
}