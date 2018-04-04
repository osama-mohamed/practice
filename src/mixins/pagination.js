export default {
  methods: {
    makePagination (res, resh) {
      let paginate = {
        current_page: res.next,
        last_page: res.count,
        next_page_url: res.next,
        previous_page_url: res.previous
      }
      this.pagination = paginate
    }
  }
}
