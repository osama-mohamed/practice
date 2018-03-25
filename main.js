let one = new Vue({
	el: '#vue-app-one',
	data: {
		title: 'Vue component one'
	},
	methods: {
	},
	computed: {
		greet: function () {
			return 'Hello from vue app one'
		}
	}
});


let two = new Vue({
	el: '#vue-app-two',
	data: {
		title: 'Vue component two'
	},
	methods: {
		changeTitle: function () {
			one.title = 'title has been changed from vue app two'
		}
	},
	computed: {
		greet: function () {
			return 'Hello from vue app two'
		}
	}
});