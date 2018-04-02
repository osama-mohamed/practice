<template>
  <div id="dashboard">
    <h3 class="center-align">Dashboard</h3>
    <ul class="collection with-header">
      <li class="collection-header"><h4 class="center-align"><i class="fa fa-users"></i> Employees</h4></li>
      <li v-for="employee in employees" v-bind:key="employee.id" class="collection-item">
        <div class="chip">{{employee.department}}</div>
        {{employee.employee_id}} : {{employee.name}}
        <router-link class="secondary-content btn blue" v-bind:to="{name: 'view-employee', params: {employee_id: employee.employee_id}}">
          View
        </router-link>
      </li>
    </ul>
    <div class="fixed-action-btn">
      <router-link v-bind:to="{name: 'new-employee'}" class="btn-floating btn-large blue">
        <i class="fa fa-plus"></i>
      </router-link>
    </div>
  </div>
</template>

<script>
import db from './firebaseInit'

export default {
  name: 'dashboard',
  data () {
    return {
      employees: []
    }
  },
  created () {
    db.collection('employees').orderBy('department').get()
      .then(querySnapshot => {
        querySnapshot.forEach(doc => {
          const data = {
            'id': doc.id,
            'employee_id': doc.data().employee_id,
            'name': doc.data().name,
            'department': doc.data().department,
            'position': doc.data().position,
          }
          this.employees.push(data)
        })
      });
  }
}
</script>

<style scoped>

</style>
