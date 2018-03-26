import Vue from 'vue'
import App from './App.vue'

import VueResource from 'vue-resource'

Vue.use(VueResource)

// Global Custom directive
Vue.directive('randomColor', {
  bind(el, binding, vnode) {
    el.style.color = '#' + Math.random().toString().slice(2, 8)
  }
});

Vue.directive('theme', {
  bind(el, binding, vnode) {
    if(binding.value == 'wide') {
      el.style.maxWidth = '1200px';
    } else if(binding.value == 'narrow') {
      el.style.maxWidth = '800px';
    }
    if(binding.arg == 'column') {
      el.style.background = '#ddd';
      el.style.padding = '20px';
    }
    if(binding.modifiers.blue === true) {
      el.style.backgroundColor = '#3467db';
    }
  }
});


new Vue({
  el: '#app',
  render: h => h(App)
})
