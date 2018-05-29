import Vue from 'vue'

export default {
  state: {
    
  },
  mutations: {
    
  },
  actions: {
    SignUp ({commit}, payload) {
      // console.log(payload)
      // console.log(this.state.shared.baseURL)
      // console.log(this.$store.state.shared.baseURL)
      Vue.http.post(`${this.state.shared.baseURL}accounts/signup/`, payload)
      // {
      //   headers: {
      //     'X-Mashape-Key': 'x1TtXXYZYemshmluWEEZ3mqnx78yp1RtL6gjsnoxDbxhy4TBoT',
      //     'Content-Type': 'application/x-www-form-urlencoded',
      //     'Accept': 'application/json'
      //   }
      // })
        .then(data => {
          console.log(data)
          console.log(data.body.message[0])
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