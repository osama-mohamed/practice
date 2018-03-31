<template>
  <div class="details">
    <router-link v-bind:to="{name: 'home'}">Back</router-link>
    <h1 class="page-header">Details</h1>
    <h1 class="page-header">{{customer.username}}
        <span class="pull-right">
          <!--<router-link class="btn btn-primary" v-bind:to="'/customer/edit/'+customer.id">Edit</router-link>-->
          <router-link class="btn btn-primary" v-bind:to="{name: 'update', params: {id: customer.id}}">Edit</router-link>
          <button class="btn btn-danger" v-on:click="deleteCustomer(customer.id)">Delete</button>
        </span>
    </h1>
    <ul class="list-group">
      <li class="list-group-item">{{customer.first_name}}</li>
      <li class="list-group-item">{{customer.last_name}}</li>
      <li class="list-group-item"><span class="glyphicon glyphicon-user" aria-hidden="true"></span> {{customer.username}}</li>
      <li class="list-group-item"><span class="glyphicon glyphicon-phone" aria-hidden="true"></span> {{customer.phone_number}}</li>
      <li class="list-group-item"><span class="glyphicon glyphicon-envelope" aria-hidden="true"></span> {{customer.email}}</li>
    </ul>

    <ul class="list-group">
      <li class="list-group-item"><span class="glyphicon glyphicon-map-marker" aria-hidden="true"></span> {{customer.address}}</li>
      <li class="list-group-item"><span class="glyphicon glyphicon-globe" aria-hidden="true"></span> {{customer.country}}</li>
      <li class="list-group-item"><span class="glyphicon glyphicon-home" aria-hidden="true"></span> {{customer.region}}</li>
    </ul>
    <ul class="list-group">
      <li class="list-group-item"><span class="glyphicon glyphicon-plus" aria-hidden="true"></span> {{customer.added}}</li>
      <li class="list-group-item"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span> {{customer.updated}}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'customerdetails',
  data () {
    return {
      customer: ''
    }
  },
  methods: {
    fetchCustomer(id) {
      this.$http.get('http://localhost:8000/api/accounts/profile/' + id + '/')
      .then(function (response) {
        this.customer = response.body;
      });
    },
    deleteCustomer(id) {
      this.$http.delete('http://localhost:8000/api/accounts/profile/delete/' + id + '/')
      .then(function (response) {
        this.$router.push({name: 'home', query: {alert: 'Customer Deleted'}})
      });
    }
  },
  created: function () {
    this.fetchCustomer(this.$route.params.id);
  }
}
</script>

<style scoped>

</style>
