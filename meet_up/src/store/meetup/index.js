import * as firebase from 'firebase'

export default {
  state: {
    loadedMeetups: []
  },
  mutations: {
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
    }
  },
  actions: {
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
      commit('setLoading', true)
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
          commit('setLoading', false)
        })
        .catch((error) => {
          console.log(error)
          commit('setLoading', false)
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
    deleteMeetup ({commit}, payload) {
      commit('setLoading', true)
      if (!payload.id) {
        return
      }
      firebase.database().ref('meetups').child(payload.id).remove()
        .then(() => {
          firebase.storage().refFromURL(payload.imageUrl).delete()
            .then(() => {
              commit('setLoading', false)
            })
            .catch((error) => {
              console.log(error)
            })
          commit('setLoading', false)
        })
        .catch((error) => {
          console.log(error)
          commit('setLoading', false)
        })
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
    }
  }
}
