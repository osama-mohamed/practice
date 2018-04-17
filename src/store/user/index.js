import * as firebase from 'firebase'

export default {
  state: {
    user: null
  },
  mutations: {
    registerMeetup (state, payload) {
      const id = payload.id
      if (state.user.registeredMeetups.findIndex(meetup => meetup.id === id) >= 0) {
        return
      }
      state.user.registeredMeetups.push(id)
      state.user.fbkeys[id] = payload.fbkey
    },
    unRegisterMeetup (state, payload) {
      const registeredMeetups = state.user.registeredMeetups
      registeredMeetups.splice(registeredMeetups.findIndex(meetup => meetup.id === payload), 1)
      Reflect.deleteProperty(state.user.fbkeys, payload)
    },
    setUser (state, payload) {
      state.user = payload
    }
  },
  actions: {
    registerMeetup ({commit, getters}, payload) {
      commit('setLoading', true)
      const user = getters.user
      firebase.database().ref('/users/' + user.id).child('/registrations/').push(payload)
        .then(data => {
          commit('setLoading', false)
          commit('registerMeetup', {id: payload, fbkey: data.key})
        })
        .catch((error) => {
          console.log(error)
          commit('setLoading', false)
        })
    },
    unRegisterMeetup ({commit, getters}, payload) {
      commit('setLoading', true)
      const user = getters.user
      if (!user.fbkeys) {
        return
      }
      const fbkey = user.fbkeys[payload]
      firebase.database().ref('/users/' + user.id + '/registrations/').child(fbkey).remove()
        .then(() => {
          commit('setLoading', false)
          commit('unRegisterMeetup', payload)
        })
        .catch((error) => {
          console.log(error)
          commit('setLoading', false)
        })
      commit('setLoading', false)
    },
    UserSignUp ({commit}, payload) {
      commit('setLoading', true)
      commit('clearError')
      firebase.auth().createUserWithEmailAndPassword(payload.email, payload.password)
        .then(
          user => {
            commit('setLoading', false)
            const newUser = {
              id: user.uid,
              registeredMeetups: [],
              fbkeys: {}
            }
            commit('setUser', newUser)
          }
        )
        .catch(error => {
          commit('setLoading', false)
          commit('setError', error)
          console.log(error)
        })
    },
    UserSignIn ({commit}, payload) {
      commit('setLoading', true)
      commit('clearError')
      firebase.auth().signInWithEmailAndPassword(payload.email, payload.password)
        .then(
          user => {
            commit('setLoading', false)
            const currentUser = {
              id: user.uid,
              registeredMeetups: [],
              fbkeys: {}
            }
            commit('setUser', currentUser)
          }
        )
        .catch(
          error => {
            commit('setLoading', false)
            commit('setError', error)
            console.log(error)
          }
        )
    },
    autoSignIn ({commit}, payload) {
      commit('setUser', {
        id: payload.uid,
        email: payload.email,
        registeredMeetups: [],
        fbkeys: {}
      })
    },
    fetchUserMeetups ({commit, getters}) {
      commit('setLoading', true)
      firebase.database().ref('/users/' + getters.user.id + '/registrations/').once('value')
        .then(data => {
          const meetupIds = data.val()
          let registeredMeetups = []
          let reversed = {}
          for (let key in meetupIds) {
            registeredMeetups.push(meetupIds[key])
            reversed[meetupIds[key]] = key
          }
          const updatedUser = {
            id: getters.user.id,
            email: getters.user.email,
            registeredMeetups: registeredMeetups,
            fbkeys: reversed
          }
          commit('setLoading', false)
          commit('setUser', updatedUser)
        })
        .catch(error => {
          commit('setLoading', false)
          commit('setError', error)
          console.log(error)
        })
    },
    logout ({commit}) {
      firebase.auth().signOut()
      commit('setUser', null)
    }
  },
  getters: {
    user (state) {
      return state.user
    }
  }
}
