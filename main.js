new Vue({
	el: '#vue-app',
	data: {
		age: 23,
		x: 0,
		y: 0
	},
	methods: {
		add: function () {
			this.age += 1
		},
		sub: function () {
			this.age -= 1
		},
		updateXY: function (e) {
			this.x = e.offsetX,
			this.y = e.offsetY
		}
	}
});