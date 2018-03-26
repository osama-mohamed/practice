<template>
   <div id="show-blogs" v-theme:column.blue="'wide'">
     <h1>All Articles</h1>
     <div v-for="blog in blogs" class="single-article">
        <h2 v-randomColor>{{ blog.title | to-uppercase}}</h2>
        <!--<h2>{{ blog.title | toUppercase}}</h2>-->
        <article>{{ blog.body | snippet}}</article>
     </div>
   </div>
</template>

<script>
export default {
  data () {
    return {
      blogs: [],
    }
  },
  methods: {
  },
  created() {
    this.$http.get('https://jsonplaceholder.typicode.com/posts').then(function (data) {
      this.blogs = data.body.slice(0, 12)
    })
  },
  filters: {      // Local Custom filter
    'to-uppercase': function (value) {
      return value.toUpperCase();
    },
    toUppercase(value) {
      return value.toUpperCase();
    },
    'snippet': function (value) {
      return value.slice(0, 100) + ' ...';
    }
  },
  directives: {    // Local Custom directive
    randomColor: {
      bind(el, binding, vnode) {
        el.style.color = '#' + Math.random().toString().slice(2, 8)
      }
    },
    theme: {
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
    }
  }
}
</script>

<style scoped>
#show-blogs{
    max-width: 800px;
    margin: 0 auto;
}
.single-article{
    padding: 20px;
    margin: 20px 0;
    box-sizing: border-box;
    background: #eee;
}
</style>
