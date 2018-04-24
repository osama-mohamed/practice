<template>
  <div id="post">
    <div class="post-thumbnail" :style="{backgroundImage: 'url(' + image + ')'}"></div>
    <section class="post-content">
      <h2>{{id}}</h2>
      <h1>{{title}}</h1>
      <p>{{content}}</p>
      <p>{{summary}}</p>
    </section>
  </div>
</template>

<script>
export default {
  asyncData (context) {
    return context.app.$storyapi.get('cdn/stories/blog/' + context.params.postId, {
      version: 'draft'
    })
      .then(res => {
        return {
              id: res.data.story.id,
              title: res.data.story.content.title,
              content: res.data.story.content.content,
              summary: res.data.story.content.summary,
              image: res.data.story.content.thumbnail
        }
      })
      .catch(res => {
        console.log(res)
        context.error({ statusCode: res.response.status, message: res.response.data })
      })
  }
}
</script>

<style scoped>
.post-thumbnail {
  width: 100%;
  height: 300px;
  background-size: cover;
  background-position: center;
}
.post-content {
  width: 80%;
  max-width: 500px;
  margin: auto;
}
.post-content p {
  white-space: pre-line;
}
</style>