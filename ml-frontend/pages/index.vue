<template>
  <MovieList :movies="movies" />
</template>

<script>
import MovieList from '~/components/MovieList.vue'
export default {
  components: { MovieList },
  data() {
    return {
      movies: []
    }
  },
  async fetch() {
    const { movies } = await this.$axios.$get('http://localhost/prediction')
    this.movies = movies
  }
}
</script>

<style>

</style>