<template>
  <v-dialog width="350px" persistent v-model="editDialog">
    <v-btn fab accent slot="activator">
      <v-icon>edit</v-icon>
    </v-btn>
    <v-card>
      <v-container>
        <v-layout row wrap>
          <v-flex xs12>
            <v-card-title>Edit Meetup</v-card-title>
          </v-flex>
        </v-layout>
        <v-divider></v-divider>
        <v-layout row wrap>
          <v-flex xs12>
            <v-card-text>
              <v-text-field
                name="title"
                id="title"
                label="Title"
                v-model="editedTitle"
                required
              >
              </v-text-field>
              <v-text-field
                name="description"
                id="Description"
                label="description"
                v-model="editedDescription"
                multi-line
                required
              >
              </v-text-field>
            </v-card-text>
          </v-flex>
        </v-layout>
        <v-divider></v-divider>
        <v-layout row wrap>
          <v-flex xs12>
            <v-card-actions>
              <v-btn flat class="primary--text" @click="onSaveChanges">Save</v-btn>
              <v-btn flat class="secondary--text darken-1" @click="closeDialog">Close</v-btn>
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
      editDialog: false,
      editedTitle: this.meetup.title,
      editedDescription: this.meetup.description
    }
  },
  methods: {
    closeDialog () {
      this.editDialog = false
      setTimeout(() => {
        this.fillDialog()
      }, 1000)
    },
    fillDialog () {
      this.editedTitle = this.meetup.title
      this.editedDescription = this.meetup.description
    },
    onSaveChanges () {
      if (this.editedTitle.trim() === '' || this.editedDescription.trim() === '') {
        alert('title and description must be filled')
        return
      }
      this.editDialog = false
      this.$store.dispatch('updateMeetupData', {
        id: this.meetup.id,
        title: this.editedTitle,
        description: this.editedDescription
      })
    }
  }
}
</script>
