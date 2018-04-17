<template>
  <v-dialog persistent v-model="deleteDialog" width="400px">
    <v-btn class="red white--text" accent slot="activator">
      Delete
    </v-btn>
    <v-card>
      <v-container>
        <v-layout row wrap>
          <v-flex xs12>
            <v-card-title>Delete Meetup</v-card-title>
          </v-flex>
        </v-layout>
        <v-divider></v-divider>
        <v-layout row wrap>
          <v-flex xs12>
            <v-card-text>Are you sure that you want to delete this meetup ?</v-card-text>
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
  props: ['meetup'],
  data () {
    return {
      deleteDialog: false
    }
  },
  methods: {
    closeDialog () {
      this.deleteDialog = false
    },
    onConfirm () {
      this.deleteDialog = false
      this.$store.dispatch('deleteMeetup', this.meetup)
      this.$store.dispatch('loadMeetups')
      this.$router.push({name: 'meetups'})
    }
  }
}
</script>

<style scoped>
</style>
