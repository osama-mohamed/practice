import Vue from 'vue'

export default {
  state: {
    checkUsername: null,
    signInError: null,
    signInErrorMessage: null,
    userData: null
  },
  mutations: {
    // setUser (state, payload) {
    //   state.user = payload
    // }
  },
  actions: {
    checkUsername ({commit}, payload) {
      let newPayload = {
        username: payload
      }
      return Vue.http.post(`${this.state.shared.baseURL}accounts/checkusername/`, newPayload)
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
        // Vue.http.post(`${this.state.shared.baseURL}accounts/signin/`, payload)
        return Vue.http.post(`${this.state.shared.baseURL}accounts/signin/`, payload)
        .then(data => {
          this.state.signInError = data.body.message.success
          this.state.signInErrorMessage = data.body.message.message
          if (sessionStorage.getItem('userToken')) {
            sessionStorage.removeItem('userToken')
            sessionStorage.setItem('userToken', data.body.user.token)
          } else {
            sessionStorage.setItem('userToken', data.body.user.token)
          }
          return data
        })
        .catch(error => {
          console.log(error)
        })
      },
      getUser ({commit}, payload) {
        // console.log('from profile vuex')
        // console.log(payload)
        Vue.http.post(`${this.state.shared.baseURL}accounts/profile/`, payload)
        .then(data => {
          // console.log('from profile response vuex')
          // console.log(data.body.user.token)
          data.headers.token = data.body.user.token
          this.state.user.userData = data.body.user
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