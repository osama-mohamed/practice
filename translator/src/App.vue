<template>
  <div id="app" class="text-center container">
    <h1>Translator</h1>
    <br>
    <TranslateForm v-on:formSubmitText="translateText"></TranslateForm>
    <TranslateOutput v-text="translatedText"></TranslateOutput>
  </div>
</template>


<script>
import TranslateForm from './components/TranslateForm'
import TranslateOutput from './components/TranslateOutput'

export default {
  name: 'App',
  components: {
    'TranslateForm': TranslateForm,
    'TranslateOutput': TranslateOutput,
  },
  data: function () {
    return {
      translatedText: ''
    }
  },
  methods: {
    translateText: function(text, language) {
      this.$http.get('https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20180331T172247Z.b7ffa34588fc5e7c.4ca270580fce69c8f33da718b689d8f02ed0c0bd&lang='
                      + language + '&text=' + text)
      .then((response) => {
        this.translatedText = response.body.text[0];
      })
    }
  }
}
</script>


<style>
body{
  background-color: #fefefe;
}
</style>
