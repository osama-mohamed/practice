<template>
  <section id="about-page" v-editable="blok">
    <h1>{{title}}</h1>
    <p>{{content}}</p>
    <p>E-mail : <a href="mailto:osama6osama6@gmail.com">OSAMA MOHAMED</a></p>
    <p>Github : <a href="https://github.com/osama-mohamed" target="_blank">OSAMA MOHAMED</a></p>
    <p>Bitbucket : <a href="https://bitbucket.org/osama-mohamed" target="_blank">OSAMA MOHAMED</a></p>
    <p>Facebook : <a href="https://www.facebook.com/osama.mohamed.ms" target="_blank">OSAMA MOHAMED</a></p>
  </section>
</template>


<script>
export default {
  asyncData (context) {
    return context.app.$storyapi.get('cdn/stories/about', {
      version: context.isDev ? 'draft' : 'published'
    })
      .then(res => {
        return {
          blok: res.data.story.content,
          title: res.data.story.content.title,
          content: res.data.story.content.content
        }
      })
  },
  mounted () {
    this.$storyblok.init()
    this.$storyblok.on('change', () => {
      location.reload(true)
    })
  }
}
</script>

<style scoped>
#about-page {
  width: 80%;
  max-width: 500px;
  margin: auto;
}
#about-page p {
  white-space: pre-line;
}
</style>