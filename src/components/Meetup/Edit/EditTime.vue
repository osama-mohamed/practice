<template>
  <v-dialog width="350px" persistent v-model="editDialog">
    <v-btn accent slot="activator">
      Edit Time
    </v-btn>
    <v-card>
      <v-container>
        <v-layout row wrap>
          <v-flex xs12>
            <v-card-title>Edit Meetup Time</v-card-title>
          </v-flex>
        </v-layout>
        <v-divider></v-divider>
        <v-layout row wrap>
          <v-flex xs12>
            <v-time-picker v-model="editTime" style="width: 100%" actions format="24hr">
              <!-- <template scope="{save, cancel}"> -->
              <template>
                <v-btn flat class="primary--text" @click="onSaveChanges">Save</v-btn>
                <v-btn flat class="secondary--text darken-1" @click="closeDialog">Close</v-btn>
              </template>
            </v-time-picker>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  props: ['meetup'],
  data () {
    return {
      editDialog: false,
      editTime: null
    }
  },
  created () {
    this.editTime = new Date(this.meetup.date)
  },
  methods: {
    closeDialog () {
      this.editDialog = false
    },
    onSaveChanges () {
      const newDate = new Date(this.meetup.date)
      const hours = this.editTime.match(/^(\d+)/)[1]
      const minutes = this.editTime.match(/:(\d+)/)[1]
      newDate.setHours(hours)
      newDate.setMinutes(minutes)
      this.editDialog = false
      this.$store.dispatch('updateMeetupData', {
        id: this.meetup.id,
        date: newDate
      })
    }
  }
}
</script>
