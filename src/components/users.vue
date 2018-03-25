<template>
  <div id="users">
    <ul>
      <li v-for="user in users" v-on:click="user.show = !user.show">
        <h2>{{user.name}}</h2>
        <h3 v-show="user.show">{{user.speciality}}</h3>
      </li>
    </ul>
    <button v-on:click="deleteUser">Delete</button>
  </div>
</template>

<script>
export default {
//  props: ['users'],
  props: {
    users: {
      type: Array,
      required: true
    }
  },
  data () {
    return {
    }
  },
  methods: {
    deleteUser: function () {
      this.users.pop();         // delete from source (ref) delete in every where
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
