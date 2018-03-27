<template>
   <div>
     <router-view></router-view>
   </div>
</template>

<script>
import addBlog from './components/addBlog'
import showBlogs from './components/showBlogs'
import listBlogs from './components/listBlogs'

export default {
  components: {
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
