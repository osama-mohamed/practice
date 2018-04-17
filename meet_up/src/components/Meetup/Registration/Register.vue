<template>
  <v-dialog persistent v-model="registerDialog" width="400px">
    <v-btn class="primary" accent slot="activator">
      {{userIsRegistered ? 'UnRegister' : 'Register'}}
    </v-btn>
    <v-card>
      <v-container>
        <v-layout row wrap>
          <v-flex xs12>
            <v-card-title v-if="userIsRegistered">UnRegister from Meetup ?</v-card-title>
            <v-card-title v-if="!userIsRegistered">Register for Meetup ?</v-card-title>
          </v-flex>
        </v-layout>
        <v-divider></v-divider>
        <v-layout row wrap>
          <v-flex xs12>
            <v-card-text>You can always change your decision later on.</v-card-text>
          </v-flex>
        </v-layout>
        <v-layout row wrap>
          <v-flex xs12>
            <v-card-actions>
              <v-btn flat class="green--text" @click="onConfirm">Confirm</v-btn>
              <v-btn flat class="red--text darken-1" @click="closeDialog">Close</v-btn>
            </v-card-actions>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  props: ['meetupId'],
  data () {
    return {
      registerDialog: false
    }
  },
  computed: {
    userIsRegistered () {
      return this.$store.getters.user.registeredMeetups.findIndex(meetupId => {
        return meetupId === this.meetupId
      }) >= 0
    }
  },
  methods: {
    closeDialog () {
      this.registerDialog = false
    },
    onConfirm () {
      if (this.userIsRegistered) {
        this.$store.dispatch('unRegisterMeetup', this.meetupId)
      } else {
        this.$store.dispatch('registerMeetup', this.meetupId)
      }
      this.registerDialog = false
    }
  }
}
</script>
