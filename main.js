new Vue({
	el: '#vue-app',
	data: {
		name: 'OSAMA',
		job: 'Python web Developer',
		facebook: 'https://www.facebook.com/osama.mohamed.ms',
		facebookTag: '<a href="https://www.facebook.com/osama.mohamed.ms">OSAMA MOHAMED</a>'
	},
	methods: {
		greet: function (name) {
			return 'Hello ' + name + ' This if function'
		}
	}
});