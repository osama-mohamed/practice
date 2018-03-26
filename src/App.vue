<template>
   <div>
      <!--<addBlog></addBlog>-->
      <showBlogs></showBlogs>
   </div>
</template>

<script>
import addBlog from './components/addBlog'
import showBlogs from './components/showBlogs'

export default {
  components: {
    'addBlog': addBlog,
    'showBlogs': showBlogs,
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
