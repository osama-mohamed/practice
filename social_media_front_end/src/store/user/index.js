import Vue from 'vue'

export default {
  state: {
    checkUsername: null
    // signUpError: null
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
      // {
      //   headers: {
      //     'X-Mashape-Key': 'x1TtXXYZYemshmluWEEZ3mqnx78yp1RtL6gjsnoxDbxhy4TBoT',
      //     'Content-Type': 'application/x-www-form-urlencoded',
      //     'Accept': 'application/json'
      //   }
      // })
        .then(data => {
          // this.$bus.$emit('signUpError', data.body)
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