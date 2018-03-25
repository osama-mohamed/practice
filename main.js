/*
const data = {	// change all elements
	name: 'OSAMA'
}
*/

Vue.component('greeting', {
	template: `<p>Hello i'm {{name}}. <button v-on:click="changeName">Change Name</button></p>`,
	data: function () {
		return {			// change one element only
			name: 'OSAMA'
		}
	},
	/*
	data: function () {
		return data			// change all elements
	},
	*/
	methods: {
		changeName: function () {
			this.name = 'OSAMA MOHAMED'
		}
	}
});

let one = new Vue({
	el: '#vue-app-one',
	data: {

	},
	methods: {
	},
	computed: {

	}
});


let two = new Vue({
	el: '#vue-app-two',
	data: {

	},
	methods: {

	},
	computed: {

	}
});