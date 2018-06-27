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
          console.log(data)
          this.state.signInError = data.body.message.success
          this.state.signInErrorMessage = data.body.message.message
          // commit('setUser', data.body.user)
          if (sessionStorage.getItem('userID') && sessionStorage.getItem('userToken')) {
            sessionStorage.removeItem('userID')
            sessionStorage.setItem('userID', data.body.user.userId)
            sessionStorage.removeItem('userToken')
            sessionStorage.setItem('userToken', data.body.user.token)
          } else {
            sessionStorage.setItem('userID', data.body.user.userId)
            sessionStorage.setItem('userToken', data.body.user.token)
          }
          return data
        })
        .catch(error => {
          console.log(error)
        })
      },
      getUser ({commit}, payload) {
        Vue.http.post(`${this.state.shared.baseURL}accounts/profile/`, payload)
        .then(data => {
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