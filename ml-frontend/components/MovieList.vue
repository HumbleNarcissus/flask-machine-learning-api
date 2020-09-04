<template>
  <v-container>
    <h1>Movies List</h1>
  </v-container>
</template>

<script>
export default {
  props: {
    movies: {
      type: Array,
      default: () => {}
    }
  }
}
</script>

<style>

</style>