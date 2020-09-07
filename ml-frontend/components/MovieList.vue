<template>
  <v-container class="movie-container">
    <v-card
      v-for="movie in movies"
      :key="movie.id"
      width="320px"
      min-height="400px"
    >
      <v-img
        class="white--text align-end"
        height="400px"
        width="320px"
        :src="movie.url"
      >
      </v-img>
      <v-card-title>{{ movie.title }}</v-card-title>
    </v-card>
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
};
</script>

<style>
.movie-container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: 16px;
}
</style>
