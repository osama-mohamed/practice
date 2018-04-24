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
  asyncData (context) {
    return context.app.$storyapi.get('cdn/stories', {
      version: 'draft',
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
      .catch(res => {
        console.log(res)
        context.error({ statusCode: res.response.status, message: res.response.data })
      })
  }
  // data () {
  //   return {
  //     posts: [
  //       {
  //         id: 'first-post',
  //         title: 'first post',
  //         previewText: 'here some text',
  //         thumbnailUrl: 'http://placehold.it/300/300'
  //       },
  //       {
  //         id: 'second-post',
  //         title: 'second post',
  //         previewText: 'here some text',
  //         thumbnailUrl: 'http://placehold.it/300/400'
  //       }
  //     ]
  //   }
  // }
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
