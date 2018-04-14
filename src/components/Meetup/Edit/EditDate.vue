<template>
  <v-dialog width="350px" persistent v-model="editDialog">
    <v-btn accent slot="activator">
      Edit Date
    </v-btn>
    <v-card>
      <v-container>
        <v-layout row wrap>
          <v-flex xs12>
            <v-card-title>Edit Meetup Date</v-card-title>
          </v-flex>
        </v-layout>
        <v-divider></v-divider>
        <v-layout row wrap>
          <v-flex xs12>
            <v-date-picker v-model="editDate" style="width: 100%" actions>
              <!-- <template scope="{save, cancel}"> -->
              <template>
                <v-btn flat class="primary--text" @click="onSaveChanges">Save</v-btn>
                <v-btn flat class="secondary--text darken-1" @click="closeDialog">Close</v-btn>
              </template>
            </v-date-picker>
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
      editDate: null
    }
  },
  // created () {
  //   this.editDate = new Date(this.meetup.date)
  // },
  methods: {
    closeDialog () {
      this.editDialog = false
    },
    onSaveChanges () {
      const newDate = new Date(this.meetup.date)
      const newDay = new Date(this.editDate).getUTCDate()
      const newMonth = new Date(this.editDate).getUTCMonth()
      const newYear = new Date(this.editDate).getUTCFullYear()
      newDate.setUTCDate(newDay)
      newDate.setUTCMonth(newMonth)
      newDate.setUTCFullYear(newYear)
      this.editDialog = false
      this.$store.dispatch('updateMeetupData', {
        id: this.meetup.id,
        date: newDate
      })
    }
  }
}
</script>
