<template>
  <div class="test">
    <input type="text" v-model="title">
    <h1>{{title}}</h1>
    <span v-html="title2"></span>
    <p>{{user.firstName}}</p>
    <p v-text="user.firstName"></p>
    <p v-if="showName">{{user.lastName}}</p>
    <p v-else="showName">Text hidden</p>
    <ul>
      <li v-for="item in items">{{item.title}}</li>
    </ul>
    <button v-on:click="greet('Hello OSAMA')">Greeting</button>
    <br>
    <br>
    <input type="text" v-on:keyup="pressKey" v-on:keyup.enter="enterHit">
    <hr>
    <label for="firstName">First Name: </label>
    <input type="text" v-model="user.firstName" id="firstName">
    <label for="lastName">Last Name: </label>
    <input type="text" v-model="user.lastName" id="lastName">
    <h3><span>Full Name is : </span>{{fullName}}</h3>
    <h3><span>Props is : </span>{{msg}}</h3>
    <hr>
  </div>
</template>

<script>
  export default {
    name: 'test',
    props: {
      msg: {
        type: String,
        default: 'Hi'
      },
    },
    data () {
      return {
        title: 'Hello OS',
        title2: '<h1>Hello OSAMA</h1>',
        user: {
          firstName: 'OSAMA',
          lastName: 'MOHAMED'
        },
        showName: false,
        items: [
          {title: 'item 1'},
          {title: 'item 2'},
          {title: 'item 3'}
        ]
      }
    },
    methods: {
      greet: function (greetText) {
        alert(greetText);
      },
      pressKey: function (e) {
        console.log(e.target.value);
      },
      enterHit: function () {
        console.log('you hit enter key');
      }
    },
    computed: {
      fullName: function () {
        return this.user.firstName + ' ' + this.user.lastName
      }
    }
  }
</script>


<style scoped>
  h1{
    color: blue
  }
</style>
