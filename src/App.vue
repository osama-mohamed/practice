<template>
  <div id="app">
    <Navbar></Navbar>
    <div class="container">
      <h3 class="text-center">Developed By : <a href="https://www.facebook.com/osama.mohamed.ms">OSAMA MOHAMED</a></h3>
      <router-view/>
    </div>
  </div>
</template>

<script>
import Navbar from './components/Navbar'

/*import fetchArticles from './mixins/fetchArticles'
import addArticle from './mixins/addArticle'
import editArticle from './mixins/editArticle'
import deleteArticle from './mixins/deleteArticle'
import pagination from './mixins/pagination'*/

export default {
  name: 'App',
  /*mixins: [
    fetchArticles,
    addArticle,
    editArticle,
    deleteArticle,
    pagination,
  ],*/
  components: {
    Navbar
  }
}
</script>

<style>

</style>
