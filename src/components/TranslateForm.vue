<template>
  <div>
  <h1>Developed By : <a href="https://www.facebook.com/osama.mohamed.ms">OSAMA MOHAMED</a></h1>
  <br>
  <div id="translateForm" class="row">
    <div class="centerForm col-sm-offset-3 col-sm-6">
      <form id="transForm" v-on:submit.prevent="formSubmit" class="form-inline jumbotron">
        <input type="text" v-model="textToTranslate" class="form-control" placeholder="Type a word...">
        <select v-model="language" class="form-control" v-on:change="formSubmit">
          <option value="ar">Arabic</option>
          <option value="en">English</option>
          <option value="fr">French</option>
          <option value="ru">Russian</option>
          <option value="de">German</option>
          <option value="it">Italian</option>
          <option value="ko">Korean</option>
          <option value="la">Latin</option>
          <option value="ja">Japanese</option>
          <option value="zh">Chinese</option>
        </select>
        <button type="submit" class="btn btn-primary">Translate</button>
      </form>
    </div>
  </div>
    </div>
</template>

<script>
export default {
  name: 'translateForm',
  data() {
    return {
      textToTranslate: '',
      language: ''
    }
  },
  created() {
    this.language = 'ar';
  },
  methods: {
    formSubmit() {
      if(!this.textToTranslate == '') {
        this.$emit('formSubmitText', this.textToTranslate, this.language);
      } else {
        alert(' Type a word then select language to translate to it \n then hit translate button')
      }
    }
  }
}
</script>

<style scoped>
#transForm{
  border-radius:10px;
  border: 1px #ccc solid;
}

.centerForm{
  margin: 0 auto;
}
.centerForm > form > input{
  min-width: 55%;
}
</style>
