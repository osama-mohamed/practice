new Vue({
	el: '#vue-app',
	data: {

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