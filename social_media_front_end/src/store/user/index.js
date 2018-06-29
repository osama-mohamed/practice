import Vue from 'vue'

export default {
  state: {
    checkUsername: null,
    signInError: null,
    signInErrorMessage: null,
    userData: null
  },
  mutations: {
    setUser (state, payload) {
      // console.log(state.userData)
      state.userData = payload
    }
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
          // commit('setUser', data.body.user)
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
    user (state) {
      return state.userData
    }
  }
}