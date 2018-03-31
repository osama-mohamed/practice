<template>
  <div class="hello">
    <div class="holder">
      <form @submit.prevent="addSkill">
        <input type="text" placeholder="Enter a skill you have ..." v-model="skill" v-validate="'min: 5'" name="skill" autocomplete="off">

        <transition name="alert-in" enter-active-class="animated flipInX" leave-active-class="animated flipOutX">
          <p class="alert" v-if="errors.has('skill')">{{errors.first('skill')}}</p>
        </transition>
      </form>
      <ul>
        <!--<li v-for="(data, index) in skills" :key="index">{{index}}. {{data.skill}}</li>-->
        <transition-group name="list" enter-active-class="animated bounceInUp" leave-active-class="animated bounceOutDown">
          <li v-for="(data, index) in skills" :key='index'>
            {{ data.skill }}
            <i class="fa fa-minus-circle" v-on:click="remove(index)"></i>
          </li>
        </transition-group>
      </ul>
      <p v-if="skills.length >= 1">You have {{skills.length}} skills</p>
      <p v-else>You do not have any skills yet</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      skill: '',
      skills: [
        {skill: 'python'},
        {skill: 'django'},
        {skill: 'flask'},
        {skill: 'jquery'},
        {skill: 'javascript'},
      ],
    }
  },
  methods: {
    addSkill () {
      this.$validator.validateAll().then((result) => {
        if (result) {
          this.skills.push({skill: this.skill});
          this.skill = '';
        } else {
          document.querySelector('form > p').textContent = 'Not valid';
        }
      })
    },
    remove(id) {
      this.skills.splice(id, 1)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style src="./skills.css" scoped>

</style>
