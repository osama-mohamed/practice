import Vue from 'vue'

export default {
  state: {
    checkUsername: null,
    signInError: null,
    signInErrorMessage: null,
    userData: localStorage.getItem('userToken') || null,
  },
  mutations: {
    setUser (state, payload) {
      state.userData = payload
    },
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
        return Vue.http.post(`${this.state.shared.baseURL}accounts/signin/`, payload)
        .then(data => {
          // this.state.user.userData = data.body.user
          // commit('setUser', data.body.user)
          this.state.user.userStatus = true
          this.state.signInError = data.body.message.success
          this.state.signInErrorMessage = data.body.message.message
          if (localStorage.getItem('userToken')) {
            localStorage.removeItem('userToken')
            localStorage.setItem('userToken', data.body.user.token)
          } else {
            localStorage.setItem('userToken', data.body.user.token)
          }
          return data
        })
        .catch(error => {
          console.log(error)
        })
      },
      SignOut ({commit}, payload) {
        return Vue.http.post(`${this.state.shared.baseURL}accounts/signout/`, payload)
        .then(data => {
          this.state.user.userData = null
          return data
        })
        .catch(error => {
          console.log(error)
        })
      },
      profile ({commit}, payload) {
        Vue.http.post(`${this.state.shared.baseURL}accounts/profile/`, payload)
        .then(data => {
          data.headers.token = data.body.user.token
          this.state.user.userData = data.body.user
          // commit('setUser', data.body.user)
          return data
        })
        .catch(error => {
          console.log(error)
        })
      },
  },
  getters: {
    userData (state) {
      return state.userData
    }
  }
}