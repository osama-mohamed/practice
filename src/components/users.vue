<template>
  <div id="users">
    <ul>
      <li v-for="user in users" v-on:click="user.show = !user.show">
        <h2>{{user.name}}</h2>
        <h3 v-show="user.show">{{user.speciality}}</h3>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data () {
    return {
      users:[
        {name: 'Osama', speciality: 'Vue Components', show: false},
        {name: 'Mohamed', speciality: 'HTML Wizardry', show: false},
        {name: 'Mahmoud', speciality: 'Click Events', show: false},
        {name: 'Ahmed', speciality: 'Conditionals', show: false},
        {name: 'Eslam', speciality: 'Webpack', show: false},
        {name: 'Nasser', speciality: 'Data Diggin', show: false}
      ]
    }
  }
}
</script>

<style scoped>
#users{
    width: 100%;
    max-width: 1200px;
    margin: 40px auto;
    padding: 0 20px;
    box-sizing: border-box;
}
ul{
    display: flex;
    flex-wrap: wrap;
    list-style-type: none;
    padding: 0;
}
li{
    flex-grow: 1;
    flex-basis: 300px;
    text-align: center;
    padding: 30px;
    border: 1px solid #222;
    margin: 10px;
}
</style>
