<template>
   <div>
        <form-helper>
            <div slot="form-header">
                <h3>This is the title of a form</h3>
                <p>This is some info about the form</p>
            </div>
            <div slot="form-fields">
                <input type="text" placeholder="name" required />
                <input type="password" placeholder="password" required />
            </div>
            <div slot="form-controls">
                <button v-on:click="">Submit</button>
            </div>
        </form-helper>
    </div>
</template>

<script>
import formHelper from './components/formHelper.vue'


export default {
  components: {
    'form-helper': formHelper,
  },
  data () {
    return {
      title: 'This is dynamic header from slot'
    }
  },
  methods: {
  }
}
</script>

<style scoped>

</style>
