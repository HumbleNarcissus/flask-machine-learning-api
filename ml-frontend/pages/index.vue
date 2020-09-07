<template>
  <MovieList :movies="movies" />
</template>

<script>
import { mapActions, mapState } from 'vuex'
import MovieList from '~/components/MovieList.vue'
export default {
  components: { MovieList },
  computed: {
    ...mapState('movies', ['movies'])
  },
  methods: {
    ...mapActions('movies', ['getMovies'])
  },
  async fetch() {
    this.getMovies()
  }
}
</script>

<style>

</style>