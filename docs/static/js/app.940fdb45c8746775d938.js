webpackJsonp([1],{"0na8":function(e,t){},"1a6f":function(e,t,a){"use strict";var n=a("qVsQ"),i={name:"view-employee",data:function(){return{employee_id:null,name:null,department:null,position:null}},beforeRouteEnter:function(e,t,a){n.a.collection("employees").where("employee_id","==",e.params.employee_id).get().then(function(e){e.forEach(function(e){a(function(t){t.employee_id=e.data().employee_id,t.name=e.data().name,t.department=e.data().department,t.position=e.data().position})})})},watch:{$route:"fetchData"},methods:{fetchData:function(){var e=this;n.a.collection("employees").where("employee_id","==",this.$route.params.employee_id).get().then(function(t){t.forEach(function(t){e.employee_id=t.data().employee_id,e.name=t.data().name,e.department=t.data().department,e.position=t.data().position})})},deleteEmployee:function(){var e=this;confirm("Are You sure ?")&&n.a.collection("employees").where("employee_id","==",this.$route.params.employee_id).get().then(function(t){t.forEach(function(t){t.ref.delete(),e.$router.push({name:"dashboard"})})})}}},o={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{attrs:{id:"view-employee"}},[a("h3",{staticClass:"center-align"},[e._v("View Employee")]),e._v(" "),a("ul",{staticClass:"collection with-header"},[a("li",{staticClass:"collection-header"},[a("h4",{staticClass:"center-align"},[a("i",{staticClass:"fa fa-user"}),e._v(" "+e._s(e.name))])]),e._v(" "),a("li",{staticClass:"collection-item"},[e._v("Employee ID#: "+e._s(e.employee_id))]),e._v(" "),a("li",{staticClass:"collection-item"},[e._v("Department: "+e._s(e.department))]),e._v(" "),a("li",{staticClass:"collection-item"},[e._v("Position: "+e._s(e.position))])]),e._v(" "),a("router-link",{staticClass:"btn ",attrs:{to:{name:"dashboard"}}},[e._v("Back")]),e._v(" "),a("button",{staticClass:"btn red",on:{click:e.deleteEmployee}},[e._v("Delete")]),e._v(" "),a("div",{staticClass:"fixed-action-btn"},[a("router-link",{staticClass:"btn-floating btn-large blue",attrs:{to:{name:"edit-employee",params:{employee_id:e.employee_id}}}},[a("i",{staticClass:"fa fa-edit"})])],1)],1)},staticRenderFns:[]};var s=a("VU/8")(i,o,!1,function(e){a("bDp+")},"data-v-274e25cc",null);t.a=s.exports},"6bic":function(e,t,a){"use strict";var n=a("qVsQ"),i={name:"edit-employee",data:function(){return{employee_id:null,name:null,department:null,position:null}},beforeRouteEnter:function(e,t,a){n.a.collection("employees").where("employee_id","==",e.params.employee_id).get().then(function(e){e.forEach(function(e){a(function(t){t.employee_id=e.data().employee_id,t.name=e.data().name,t.department=e.data().department,t.position=e.data().position})})})},watch:{$route:"fetchData"},methods:{fetchData:function(){var e=this;n.a.collection("employees").where("employee_id","==",this.$route.params.employee_id).get().then(function(t){t.forEach(function(t){e.employee_id=t.data().employee_id,e.name=t.data().name,e.department=t.data().department,e.position=t.data().position})})},updateEmployee:function(){var e=this;n.a.collection("employees").where("employee_id","==",this.$route.params.employee_id).get().then(function(t){t.forEach(function(t){t.ref.update({employee_id:e.employee_id,name:e.name,department:e.department,position:e.position}).then(function(){e.$router.push({name:"view-employee",params:{employee_id:e.employee_id}})})})})}}},o={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{attrs:{id:"edit-employee"}},[a("h3",[e._v("Edit Employee")]),e._v(" "),a("div",{staticClass:"row"},[a("form",{staticClass:"col s12",on:{submit:function(t){return t.preventDefault(),e.updateEmployee(t)}}},[a("div",{staticClass:"row"},[a("div",{staticClass:"input-field col s12"},[a("input",{directives:[{name:"model",rawName:"v-model",value:e.employee_id,expression:"employee_id"}],attrs:{type:"text",required:""},domProps:{value:e.employee_id},on:{input:function(t){t.target.composing||(e.employee_id=t.target.value)}}})])]),e._v(" "),a("div",{staticClass:"row"},[a("div",{staticClass:"input-field col s12"},[a("input",{directives:[{name:"model",rawName:"v-model",value:e.name,expression:"name"}],attrs:{type:"text",required:""},domProps:{value:e.name},on:{input:function(t){t.target.composing||(e.name=t.target.value)}}})])]),e._v(" "),a("div",{staticClass:"row"},[a("div",{staticClass:"input-field col s12"},[a("input",{directives:[{name:"model",rawName:"v-model",value:e.department,expression:"department"}],attrs:{type:"text",required:""},domProps:{value:e.department},on:{input:function(t){t.target.composing||(e.department=t.target.value)}}})])]),e._v(" "),a("div",{staticClass:"row"},[a("div",{staticClass:"input-field col s12"},[a("input",{directives:[{name:"model",rawName:"v-model",value:e.position,expression:"position"}],attrs:{type:"text",required:""},domProps:{value:e.position},on:{input:function(t){t.target.composing||(e.position=t.target.value)}}})])]),e._v(" "),a("button",{staticClass:"btn blue",attrs:{type:"submit"}},[e._v("Edit Employee")]),e._v(" "),a("router-link",{staticClass:"btn",attrs:{to:{name:"dashboard"}}},[e._v("Cancel")])],1)])])},staticRenderFns:[]};var s=a("VU/8")(i,o,!1,function(e){a("yWP/")},"data-v-5056f8a4",null);t.a=s.exports},NHnr:function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var n=a("7+uW"),i={render:function(){var e=this.$createElement,t=this._self._c||e;return t("nav",[t("div",{staticClass:"nav-wrapper blue"},[t("div",{staticClass:"container"},[t("router-link",{staticClass:"brand-logo",attrs:{to:"/"}},[this._v("Employee Manager")])],1)])])},staticRenderFns:[]},o={name:"App",components:{Navbar:a("VU/8")(null,i,!1,null,null,null).exports}},s={render:function(){var e=this.$createElement,t=this._self._c||e;return t("div",{attrs:{id:"app"}},[t("Navbar"),this._v(" "),t("div",{staticClass:"container"},[t("router-view")],1)],1)},staticRenderFns:[]};var l=a("VU/8")(o,s,!1,function(e){a("0na8")},null,null).exports,r=a("YaEn");n.a.config.productionTip=!1,new n.a({el:"#app",router:r.a,components:{App:l},template:"<App/>"})},TGvd:function(e,t,a){"use strict";var n=a("qVsQ"),i={name:"dashboard",data:function(){return{employees:[]}},created:function(){var e=this;n.a.collection("employees").orderBy("department").get().then(function(t){t.forEach(function(t){var a={id:t.id,employee_id:t.data().employee_id,name:t.data().name,department:t.data().department,position:t.data().position};e.employees.push(a)})})}},o={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{attrs:{id:"dashboard"}},[a("h3",{staticClass:"center-align"},[e._v("Dashboard")]),e._v(" "),a("ul",{staticClass:"collection with-header"},[e._m(0),e._v(" "),e._l(e.employees,function(t){return a("li",{key:t.id,staticClass:"collection-item"},[a("div",{staticClass:"chip"},[e._v(e._s(t.department))]),e._v("\n      "+e._s(t.employee_id)+" : "+e._s(t.name)+"\n      "),a("router-link",{staticClass:"secondary-content btn blue",attrs:{to:{name:"view-employee",params:{employee_id:t.employee_id}}}},[e._v("\n        View\n      ")])],1)})],2),e._v(" "),a("div",{staticClass:"fixed-action-btn"},[a("router-link",{staticClass:"btn-floating btn-large blue",attrs:{to:{name:"new-employee"}}},[a("i",{staticClass:"fa fa-plus"})])],1)])},staticRenderFns:[function(){var e=this.$createElement,t=this._self._c||e;return t("li",{staticClass:"collection-header"},[t("h4",{staticClass:"center-align"},[t("i",{staticClass:"fa fa-users"}),this._v(" Employees")])])}]};var s=a("VU/8")(i,o,!1,function(e){a("Up9X")},"data-v-762be9cc",null);t.a=s.exports},Up9X:function(e,t){},YaEn:function(e,t,a){"use strict";(function(e){var n=a("7+uW"),i=a("/ocq"),o=a("TGvd"),s=a("xWWj"),l=a("1a6f"),r=a("6bic");n.a.use(i.a),t.a=new i.a({mode:"history",base:e,routes:[{path:"/employee_manager_vue/",name:"dashboard",component:o.a},{path:"/employee_manager_vue/new",name:"new-employee",component:s.a},{path:"/employee_manager_vue/edit/:employee_id",name:"edit-employee",component:r.a},{path:"/employee_manager_vue/:employee_id",name:"view-employee",component:l.a}]})}).call(t,"/")},"bDp+":function(e,t){},qVsQ:function(e,t,a){"use strict";var n=a("Sazm"),i=a.n(n),o=(a("3VHS"),i.a.initializeApp({apiKey:"AIzaSyDqBxo82epuwztS2hKQ-jh6dzImDMJL2jU",authDomain:"vue-osama.firebaseapp.com",databaseURL:"https://vue-osama.firebaseio.com",projectId:"vue-osama",storageBucket:"vue-osama.appspot.com",messagingSenderId:"465272663405"}));t.a=o.firestore()},xWWj:function(e,t,a){"use strict";var n=a("qVsQ"),i={name:"new-employee",data:function(){return{employee_id:null,name:null,department:null,position:null}},methods:{newEmployee:function(){var e=this;n.a.collection("employees").add({employee_id:this.employee_id,name:this.name,department:this.department,position:this.position}).then(function(t){return e.$router.push({name:"dashboard"})}).catch(function(e){return alert(e)})}}},o={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{attrs:{id:"new-employee"}},[a("h3",[e._v("Add New Employee")]),e._v(" "),a("div",{staticClass:"row"},[a("form",{staticClass:"col s12",on:{submit:function(t){return t.preventDefault(),e.newEmployee(t)}}},[a("div",{staticClass:"row"},[a("div",{staticClass:"input-field col s12"},[a("input",{directives:[{name:"model",rawName:"v-model",value:e.employee_id,expression:"employee_id"}],attrs:{type:"text",required:""},domProps:{value:e.employee_id},on:{input:function(t){t.target.composing||(e.employee_id=t.target.value)}}}),e._v(" "),a("label",[e._v("Employee ID#")])])]),e._v(" "),a("div",{staticClass:"row"},[a("div",{staticClass:"input-field col s12"},[a("input",{directives:[{name:"model",rawName:"v-model",value:e.name,expression:"name"}],attrs:{type:"text",required:""},domProps:{value:e.name},on:{input:function(t){t.target.composing||(e.name=t.target.value)}}}),e._v(" "),a("label",[e._v("Name")])])]),e._v(" "),a("div",{staticClass:"row"},[a("div",{staticClass:"input-field col s12"},[a("input",{directives:[{name:"model",rawName:"v-model",value:e.department,expression:"department"}],attrs:{type:"text",required:""},domProps:{value:e.department},on:{input:function(t){t.target.composing||(e.department=t.target.value)}}}),e._v(" "),a("label",[e._v("Department")])])]),e._v(" "),a("div",{staticClass:"row"},[a("div",{staticClass:"input-field col s12"},[a("input",{directives:[{name:"model",rawName:"v-model",value:e.position,expression:"position"}],attrs:{type:"text",required:""},domProps:{value:e.position},on:{input:function(t){t.target.composing||(e.position=t.target.value)}}}),e._v(" "),a("label",[e._v("Position")])])]),e._v(" "),a("button",{staticClass:"btn blue",attrs:{type:"submit"}},[e._v("Add New Employee")]),e._v(" "),a("router-link",{staticClass:"btn",attrs:{to:{name:"dashboard"}}},[e._v("Cancel")])],1)])])},staticRenderFns:[]};var s=a("VU/8")(i,o,!1,function(e){a("zZ64")},"data-v-35342bac",null);t.a=s.exports},"yWP/":function(e,t){},zZ64:function(e,t){}},["NHnr"]);
//# sourceMappingURL=app.940fdb45c8746775d938.js.map