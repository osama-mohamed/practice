import Vue from 'vue'

export default {
  state: {
    // signUpError: null
  },
  mutations: {
    
  },
  actions: {
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