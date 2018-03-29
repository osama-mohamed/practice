<template>
  <div class="customers">
    <Alert v-if="alert" v-bind:message="alert"></Alert>
    <h1 class="page-header">Manage Customers</h1>
    <input type="text" class="form-control" placeholder="Enter Last Name" v-model="filterInput">
    <table class="table table-striped">
      <thead>
        <tr>
          <th>First Name</th>
          <th>Last Name</th>
          <th>Email</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <!--<tr>
          <td>{{customersList}}</td>
        </tr>-->
        <tr v-for="customer in filterBy(customersList, filterInput)">
          <td>{{customer.first_name}}</td>
          <td>{{customer.last_name}}</td>
          <td>{{customer.email}}</td>
          <!--<td><router-link class="btn btn-default" v-bind:to="'/customer/'+customer.id">View</router-link></td>-->
          <td><router-link class="btn btn-default" v-bind:to="{name: 'detail', params:{id: customer.id}}">View</router-link></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import Alert from './Alert'
export default {
  name: 'customers',
  data () {
    return {
      customersList: [],
      alert: '',
      filterInput: ''
    }
  },
  methods: {
    fetchCustomers() {
      this.$http.get('http://localhost:8000/api/accounts/users/all/').then(function (response) {
        return response.json();
      })
      .then(function (response) {
        this.customersList = response;
      });
    },
    filterBy(list, value) {
//      value = value.charAt(0).toUpperCase() + value.slice(1);
      return list.filter(function (customer) {
        return customer.last_name.indexOf(value) > -1;
      })
    }
  },
  created: function () {
    if(this.$route.query.alert) {
      this.alert = this.$route.query.alert;
    }
    this.fetchCustomers();
  },
  updated: function () {
    this.fetchCustomers();
  },
  components: {
    Alert
  }
}
</script>

<style scoped>

</style>
