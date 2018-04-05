<template>
  <nav class="navbar navbar-expand-sm navbar-dark bg-info mb-2">
    <div class="container">
      <a href="" class="navbar-brand">Articles</a>
      <router-link v-bind:to="{name: 'articles'}" class="text-light">Articles</router-link>
      <router-link v-bind:to="{name: 'about'}" class="text-light">About</router-link>
    </div>
  </nav>
</template>
