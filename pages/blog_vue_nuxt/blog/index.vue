<template>
  <section id="posts">
    <PostPreview
      v-for='post in posts'
      :key='post.id'
      :id="'/blog_vue_nuxt/blog/' + post.id"
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
  asyncData (context) {
    return context.app.$storyapi.get('cdn/stories', {
      version: context.isDev ? 'draft' : 'published',
      starts_with: 'blog/'
    })
      .then(res => {
        return {
          posts: res.data.stories.map(blogPost => {
            return {
              id: blogPost.slug,
              title: blogPost.content.title,
              previewText: blogPost.content.summary,
              thumbnailUrl: blogPost.content.thumbnail
            }
          })
        }
      })
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
