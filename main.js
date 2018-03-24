new Vue({
	el: '#vue-app',
	data: {
		name: 'OSAMA',
		job: 'Python web Developer'
	},
	methods: {
		greet: function (name) {
			return 'Hello ' + name + ' This if function'
		}
	}
});