<template>
  <section id="posts">
    <PostPreview
      v-for='post in posts'
      :key='post.id'
      :id='post.id'
      :title='post.title'
      :excerpt='post.previewText'
      :thumbnailImage='post.thumbnailUrl'
    ></PostPreview>
  </section>
</template>

<script>
import PostPreview from '@/components/Blog/PostPreview'

export default {
  components: {
    PostPreview
  },
  data () {
    return {
      posts: [
        {
          id: 'first-post',
          title: 'first post',
          previewText: 'here some text',
          thumbnailUrl: 'http://placehold.it/300/300'
        },
        {
          id: 'second-post',
          title: 'second post',
          previewText: 'here some text',
          thumbnailUrl: 'http://placehold.it/300/400'
        }
      ]
    }
  }
}
</script>

<style scoped>
#posts {
  padding-top: 2rem;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
@media (min-width: 55rem) {
  #posts {
    flex-direction: row;
  }
}
</style>
