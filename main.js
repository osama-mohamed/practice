new Vue({
	el: '#vue-app',
	data: {
		os: true,
		available: false,
		nearby: true
	},
	methods: {

	},
	computed: {
		compClasses: function () {
			return {
				available: this.available,
				nearby: this.nearby
			}
		}
	}
});