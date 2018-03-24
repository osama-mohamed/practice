<template>
  <div class="users">
    <h1>Users</h1>
    <form v-on:submit="addUser">
      <input type="text" v-model="newUser.name" placeholder="Your Name">
      <input type="text" v-model="newUser.email" placeholder="Your email">
      <input type="submit" value="Create">
    </form>
    <ul>
      <li v-for="user in users">
        <input type="checkbox" class="toggle" v-model="user.contacted">
        <span :class="{contacted: user.contacted}">
          {{user.name}} : {{user.email}} <!--: {{user.contacted}}-->
          <button v-on:click="deleteUser(user)">X</button>
        </span>
      </li>
    </ul>
  </div>
</template>


<script>
  export default {
    name: 'users',
    data () {
      return {
        newUser: {},
        users: [
/*          {
            name: 'OSAMA MOHAMED',
            email: 'osama6osama6@gmail.com',
            contacted: false
          },
          {
            name: 'AHMED MOHAMED',
            email: 'ahmed@gmail.com',
            contacted: false
          },
          {
            name: 'MAHMOUD MOHAMED',
            email: 'mahmoud@gmail.com',
            contacted: false
          }*/
        ]
      }
    },
    methods: {
      addUser: function (e) {
        e.preventDefault();
        this.users.push({
          name: this.newUser.name,
          email: this.newUser.email,
          contacted: false
        });
      },
      deleteUser: function (user) {
        this.users.splice(this.users.indexOf(user), 1);
      }
    },
    created: function () {
      this.$http.get('http://jsonplaceholder.typicode.com/users')
        .then(function (response) {
          this.users = response.data
        })
    }
  }
</script>


<style scoped>
  .contacted{
    text-decoration: line-through;
  }
</style>
