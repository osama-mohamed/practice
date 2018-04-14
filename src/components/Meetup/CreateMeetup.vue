<template>
  <v-container>
    <v-layout row>
      <v-flex  xs12 sm6 offset-sm3>
        <h2 class="primary--text">create a new meetup</h2>
      </v-flex>
    </v-layout>
    <v-layout row>
      <v-flex xs12>
        <form @submit.prevent="onCreateMeetup">
          <v-layout row>
            <v-flex xs12 sm6 offset-sm3>
              <v-text-field
                name="title"
                id="title"
                label="Title"
                v-model="title"
                required
              >
              </v-text-field>
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs12 sm6 offset-sm3>
              <v-text-field
                name="location"
                id="location"
                label="Location"
                v-model="location"
                required
              >
              </v-text-field>
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs12 sm6 offset-sm3>
              
              <!-- <v-text-field
                name="imageUrl"
                id="image-url"
                label="Image"
                v-model="imageUrl"
                required
              >
              </v-text-field> -->
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs12 sm6 offset-sm3>
              <img :src="imageUrl" height="150">
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs12 sm6 offset-sm3>
              <v-text-field
                name="description"
                id="Description"
                label="description"
                v-model="description"
                multi-line
                required
              >
              </v-text-field>
            </v-flex>
          </v-layout>
          <v-layout row justify-center>
            <v-flex xs12 sm6 offset-sm-3>
              <h4>Choose Date & Time</h4>
            </v-flex>
          </v-layout>
          <v-layout row justify-center class="mb-2">
            <v-flex xs12 sm6 offset-sm-3>
              <v-date-picker v-model="date"></v-date-picker>
              <p>{{date}}</p>
            </v-flex>
          </v-layout>
          <v-layout row justify-center>
            <v-flex xs12 sm6 offset-sm-3>
              <v-time-picker v-model="time" format="24hr"></v-time-picker>
              <p>{{time}}</p>
            </v-flex>
          </v-layout>
          <v-layout row justify-center>
            <v-flex xs12 sm6 offset-sm-3>
              <v-btn type="submit" class="primary" :disabled="!formIsValid">Create Meetup</v-btn>
              {{submittableDateTime}}
            </v-flex>
          </v-layout>
        </form>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data () {
    return {
      title: '',
      location: '',
      description: '',
      imageUrl: '',
      date: '',
      time: new Date()
    }
  },
  computed: {
    formIsValid () {
      return this.title !== '' && this.location !== '' && this.description !== '' && this.imageUrl !== ''
    },
    submittableDateTime () {
      const date = new Date(this.date)
      if (typeof (this.time) === 'string') {
        let hours = this.time.match(/^(\d+)/)[1]
        const minutes = this.time.match(/:(\d+)/)[1]
        date.setHours(hours)
        date.setMinutes(minutes)
      } else {
        date.setHours(this.time.getHours())
        date.setMinutes(this.time.getMinutes())
      }
      return date
    }
  },
  methods: {
    onCreateMeetup () {
      if (!this.formIsValid) {
        return
      }
      const meetupData = {
        title: this.title,
        location: this.location,
        description: this.description,
        imageUrl: this.imageUrl,
        date: this.submittableDateTime
      }
      this.$store.dispatch('createMeetup', meetupData)
      this.$router.push({name: 'meetups'})
    }
  }
}
</script>

<style scoped>
</style>
