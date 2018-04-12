import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    loadedMeetups: [
      { imageUrl: 'http://placehold.it/300/300', id: 'fgsgs', title: 'hgfhgdgfdsgfsgf', date: '2018-04-12' },
      { imageUrl: 'http://placehold.it/400/333', id: 'fgjhfhjfsgs', title: 'hgfhgdgfdjhghjfhjsgfsgf', date: '2018-04-11' }
    ],
    user: {
      id: 'hjvhvjhvhjvjhv',
      registeredMeetups: ['hfhdrdrtsfdgdg']
    }
  },
  mutations: {},
  actions: {},
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
