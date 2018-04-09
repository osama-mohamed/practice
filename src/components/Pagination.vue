<template>
  <div>
    <h2 class="text-center mb-4">Articles</h2>
    <h4 class="text-center mb-4">Number Of Articles is : {{pagination.last_page}}</h4>
    <nav aria-label="Page navigation example">
      <ul class="pagination">
        <li v-bind:class="[{disabled: !pagination.previous_page_url}]" class="page-item">
          <a class="page-link" href="#" @click.prevent="fetchArticles(pagination.previous_page_url.substring(0, pagination.previous_page_url.indexOf('l/')) + 'l/')">First Page</a>
        </li>
        <li v-bind:class="[{disabled: !pagination.previous_page_url}]" class="page-item">
          <a class="page-link" href="#" @click.prevent="fetchArticles(pagination.previous_page_url)">Previous</a>
        </li>


        <li class="page-item disabled" v-if="pagination.current_page && Number.isInteger(pagination.last_page/pagePagination)">
          <a class="page-link text-dark" href="#">
            Page {{pagination.current_page.substring(pagination.current_page.indexOf('=') +1) -1}}
            of {{Math.round(pagination.last_page /pagePagination)}}
          </a>
        </li>
        <li class="page-item disabled" v-else-if="!pagination.current_page && Number.isInteger(pagination.last_page/pagePagination)">
          <a class="page-link text-dark" href="#">
            Page {{Math.round(pagination.last_page /pagePagination)}}
            of {{Math.round(pagination.last_page /pagePagination)}}</a>
        </li>

        <li class="page-item disabled" v-else-if="pagination.current_page && pagination.last_page">
          <a class="page-link text-dark" href="#">
            Page {{Math.round(pagination.current_page.substring(pagination.current_page.indexOf('=') +1) -1)}}
            of {{Math.floor(pagination.last_page /pagePagination)+1}}
          </a>
        </li>
        <li class="page-item disabled" v-else-if="!pagination.current_page && pagination.last_page">
          <a class="page-link text-dark" href="#">
            Page {{Math.floor(pagination.last_page /pagePagination)+1}}
            of {{Math.floor(pagination.last_page /pagePagination)+1}}</a>
        </li>

        <li v-bind:class="[{disabled: !pagination.next_page_url}]" class="page-item">
          <a class="page-link" href="#" @click.prevent="fetchArticles(pagination.next_page_url)">Next</a>
        </li>


        <li v-bind:class="[{disabled: !pagination.next_page_url}]" class="page-item" v-if="Number.isInteger(pagination.last_page/pagePagination)">
          <a class="page-link" href="#" @click.prevent="fetchArticles(pagination.next_page_url.substring(0, pagination.next_page_url.indexOf('=')) + '=' + Math.round(pagination.last_page/pagePagination))">Last Page</a>
        </li>
        <li v-bind:class="[{disabled: !pagination.next_page_url}]" class="page-item" v-else-if="pagination.last_page">
          <a class="page-link" href="#" @click.prevent="fetchArticles(pagination.next_page_url.substring(0, pagination.next_page_url.indexOf('=')) + '=' + Math.floor(pagination.last_page/pagePagination+1))">Last Page</a>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'pagination',
  props: ['articleList'],
  watch: {
    'articleList': 'makePagination'
  },
  data () {
    return {
      pagination: {},
      pagePagination: 5,
    }
  },
  methods: {
    makePagination () {
      let paginate = {
        current_page: this.articleList.next,
        last_page: this.articleList.count,
        next_page_url: this.articleList.next,
        previous_page_url: this.articleList.previous
      }
      this.pagination = paginate
    },
    fetchArticles (e) {
      this.$emit('paginationPages', e)
    }
  }
}
</script>

<style scoped>
ul {
  display: table;
  margin: 20px auto;
}
ul li {
  display: table-cell;
}

</style>
