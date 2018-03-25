new Vue({
	el: '#vue-app',
	data: {
		name: '',
		age: ''
	},
	methods: {
		showName: function (e) {
			console.log(e.target.value)
		},
		showAge: function (e) {
			console.log(e.target.value)
		}
	},
});