<template>
   <div id="add-blog">
        <h2>Add a New Blog Post</h2>
        <form>
            <label>Blog Title:</label>
            <input type="text" required v-model.lazy="blog.title"/>
            <label>Blog Content:</label>
            <textarea v-model.lazy="blog.content"></textarea>
            <div id="checkboxes">
                <p>Blog Categories:</p>
                <label for="programming">Programming</label>
                <input type="checkbox" id='programming' value="programming" v-model="blog.categories"/>
                <label for="development">Development</label>
                <input type="checkbox" id='development' value="development" v-model="blog.categories"/>
                <label for="design">Design</label>
                <input type="checkbox" id='design' value="design" v-model="blog.categories"/>
                <label for="network">Network</label>
                <input type="checkbox" id='network' value="network" v-model="blog.categories"/>
            </div>
            <label for="">Author : </label>
            <select name="" id="" v-model="blog.author">
              <option v-for="author in authors" v-bind:value="author">{{ author.toUpperCase() }}</option>
            </select>
        </form>
        <div id="preview">
            <h3>Preview blog</h3>
            <p>Blog title: {{blog.title}}</p>
            <p>Blog content:</p>
            <p style="white-space: pre">{{blog.content}}</p>
            <p>Blog Catigories :</p>
            <ul>
                <li v-for="category in blog.categories">{{ category }}</li>
            </ul>
            <p>Author: {{ blog.author.toUpperCase() }}</p>
        </div>
    </div>
</template>

<script>


export default {
  components: {

  },
  data () {
    return {
      blog: {
        title: '',
        content: '',
        categories: [],
        author: '',
      },
      authors: ['osama', 'mohamed', 'mahmoud', 'ahmed']
    }
  },
  methods: {
  }
}
</script>

<style scoped>
#add-blog *{
    box-sizing: border-box;
}

#add-blog{
    margin: 20px auto;
    max-width: 500px;
}

label{
    display: block;
    margin: 20px 0 10px;
}

input[type="text"], textarea{
    display: block;
    width: 100%;
    padding: 8px;
}

#preview{
    padding: 10px 20px;
    border: 1px dotted #ccc;
    margin: 30px 0;
}

h3{
    margin-top: 10px;
}

#checkboxes input{
    display: inline-block;
    margin-right: 10px;
}

#checkboxes label{
    display: inline-block;
}
</style>
