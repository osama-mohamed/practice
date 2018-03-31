<template>
   <div>
     <app-header></app-header>
     <router-view></router-view>
   </div>
</template>

<script>
import header from './components/header'
import addBlog from './components/addBlog'
import showBlogs from './components/showBlogs'
import listBlogs from './components/listBlogs'

export default {
  components: {
    'app-header': header,
    'addBlog': addBlog,
    'showBlogs': showBlogs,
    'listBlogs': listBlogs
  },
  data () {
    return {
    }
  },
  methods: {
  }
}
</script>

<style scoped>

</style>
