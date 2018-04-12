import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    loadedMeetups: [
      {imageUrl: 'http://placehold.it/300/300', id: 'fgsgs', title: 'hgfhgdgfdsgfsgf', date: new Date(), location: 'cairo', describtion: 'desc here1'},
      {imageUrl: 'http://placehold.it/400/333', id: 'fgjhfhjfsgs', title: 'hgfhgdgfdjhghjfhjsgfsgf', date: new Date(), location: 'fayoum', describtion: 'desc here2'}
    ],
    user: {
      id: 'hjvhvjhvhjvjhv',
      registeredMeetups: ['hfhdrdrtsfdgdg']
    }
  },
  mutations: {
    createMeetup (state, payload) {
      state.loadedMeetups.push(payload)
    }
  },
  actions: {
    createMeetup ({commit}, payload) {
      const meetup = {
        title: payload.title,
        location: payload.location,
        description: payload.description,
        imageUrl: payload.imageUrl,
        date: payload.date,
        id: 'kgyufufuyfvjvvhj'
      }
      commit('CreateMeetup', meetup)
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
})
