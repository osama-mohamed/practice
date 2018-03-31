<template>
  <div class="edit">
    <Alert v-if="alert" v-bind:message="alert"></Alert>
    <h1 class="page-header">Edit Customer</h1>
    <form v-on:submit="updateCustomer">
        <div class="well">
            <h4>Customer Info</h4>
            <div class="form-group">
                <label>First Name</label>
                <input type="text" class="form-control" placeholder="First Name" v-model="customer.first_name">
            </div>
            <div class="form-group">
                <label>Last Name</label>
                <input type="text" class="form-control" placeholder="Last Name" v-model="customer.last_name">
            </div>
            <div class="form-group">
                <label>Username</label>
                <input type="text" class="form-control" placeholder="Username" v-model="customer.username">
            </div>
        </div>
        <div class="well">
            <h4>Customer Contact</h4>
            <div class="form-group">
                <label>Email</label>
                <input type="text" class="form-control" placeholder="Email" v-model="customer.email">
            </div>
            <div class="form-group">
                <label>Phone</label>
                <input type="text" class="form-control" placeholder="Phone" v-model="customer.phone_number">
            </div>
        </div>

        <div class="well">
            <h4>Customer Location</h4>
            <div class="form-group">
                <label>Address</label>
                <input type="text" class="form-control" placeholder="Address" v-model="customer.address">
            </div>
            <div class="form-group">
                <label>City</label>
                <input type="text" class="form-control" placeholder="City" v-model="customer.country">
            </div>
            <div class="form-group">
                <label>State</label>
                <input type="text" class="form-control" placeholder="State" v-model="customer.region">
            </div>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import Alert from './Alert'

export default {
  name: 'edit',
  data () {
    return {
      customer: {},
      alert: ''
    }
  },
  methods: {
    fetchCustomer(id) {
      this.$http.get('http://localhost:8000/api/accounts/profile/' + id + '/')
      .then(function (response) {
        this.customer = response.body;
      });
    },
    updateCustomer(e) {
      if(!this.customer.first_name ||
         !this.customer.last_name ||
         !this.customer.email) {
        this.alert = 'Fill out these fields';
      } else {
        let updatedCustomer = {
          first_name: this.customer.first_name,
          last_name: this.customer.last_name,
          phone_number: this.customer.phone_number,
          email: this.customer.email,
          username: this.customer.username,
          address: this.customer.address,
          country: this.customer.country,
          region: this.customer.region
        };
        this.$http.put('http://localhost:8000/api/accounts/profile/update/' + this.$route.params.id + '/', updatedCustomer)
          .then(function () {
            console.log(this.$route.params.id);
            this.$router.push({name: 'home', query: {alert: 'Customer Updated'}})
          });
        e.preventDefault();
      }
      e.preventDefault();

    }
  },
  created: function () {
    this.fetchCustomer(this.$route.params.id);
  },
  components: {
    Alert
  }
}
</script>

<style scoped>

</style>
