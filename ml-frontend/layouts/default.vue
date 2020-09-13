<template>
  <v-app data-app>
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
</style>