<template>
  <v-app data-app class="app">
    <navbar />
    <nuxt />
  </v-app>
</template>

<script>
import navbar from '~/components/navbar.vue'

export default {
  components: { navbar }
}
</script>

<style>
  .app {
    height: 100vh;
  }
</style>