import Vue from 'vue'
import Vuex from 'vuex'
import * as firebase from 'firebase'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    loadedMeetups: [],
    user: null,
    loading: false,
    error: null
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
    setLoadedMeetups (state, payload) {
      state.loadedMeetups = payload
    },
    createMeetup (state, payload) {
      state.loadedMeetups.push(payload)
    },
    updateMeetup (state, payload) {
      const meetup = state.loadedMeetups.find(meetup => {
        return meetup.id === payload.id
      })
      if (payload.title) {
        meetup.title = payload.title
      }
      if (payload.description) {
        meetup.description = payload.description
      }
      if (payload.date) {
        meetup.date = payload.date
      }
    },
    setUser (state, payload) {
      state.user = payload
    },
    setLoading (state, payload) {
      state.loading = payload
    },
    setError (state, payload) {
      state.error = payload
    },
    clearError (state) {
      state.error = null
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
    loadMeetups ({commit}) {
      // firebase.database().ref('meetups').on('value')  // live update from firebase database
      commit('setLoading', true)
      firebase.database().ref('meetups').once('value')
        .then((data) => {
          const meetups = []
          const obj = data.val()
          for (let key in obj) {
            meetups.push({
              id: key,
              title: obj[key].title,
              description: obj[key].description,
              location: obj[key].location,
              imageUrl: obj[key].imageUrl,
              date: obj[key].date,
              creatorId: obj[key].creatorId
            })
          }
          commit('setLoading', false)
          commit('setLoadedMeetups', meetups)
        })
        .catch((error) => {
          console.log(error)
          commit('setLoading', false)
        })
    },
    createMeetup ({commit, getters}, payload) {
      const meetup = {
        title: payload.title,
        location: payload.location,
        description: payload.description,
        date: payload.date.toISOString(),
        // creatorId: getters.user.id
        creatorId: firebase.auth().currentUser.uid
      }
      let imageUrl
      let key
      firebase.database().ref('meetups').push(meetup)
        .then((data) => {
          key = data.key
          return key
        })
        .then(key => {
          const filename = payload.image.name
          const ext = filename.slice(filename.lastIndexOf('.'))
          return firebase.storage().ref('meetups/' + key + '.' + ext).put(payload.image)
        })
        .then(fileData => {
          imageUrl = fileData.downloadURL
          return firebase.database().ref('meetups').child(key).update({
            imageUrl: imageUrl
          })
        })
        .then(() => {
          commit('createMeetup', {
            ...meetup,
            id: key,
            imageUrl: imageUrl
          })
        })
        .catch((error) => {
          console.log(error)
        })
    },
    updateMeetupData ({commit}, payload) {
      commit('setLoading', true)
      const updateobj = {}
      if (payload.title) {
        updateobj.title = payload.title
      }
      if (payload.description) {
        updateobj.description = payload.description
      }
      if (payload.date) {
        updateobj.date = payload.date
      }
      firebase.database().ref('meetups').child(payload.id).update(updateobj)
        .then(() => {
          commit('setLoading', false)
          commit('updateMeetup', payload)
        })
        .catch(error => {
          commit('setLoading', false)
          console.log(error)
        })
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
    },
    clearError ({commit}) {
      commit('clearError')
    }
  },
  getters: {
    loadedMeetups (state) {
      return state.loadedMeetups.sort((meetupA, meetupB) => {
        return meetupA.date > meetupB.date
      })
    },
    featuredMeetups (state, getters) {
      return getters.loadedMeetups.slice(0, 5)
    },
    loadedMeetup (state) {
      return (meetupId) => {
        return state.loadedMeetups.find((meetup) => {
          return meetup.id === meetupId
        })
      }
    },
    user (state) {
      return state.user
    },
    loading (state) {
      return state.loading
    },
    error (state) {
      return state.error
    }
  }
})
