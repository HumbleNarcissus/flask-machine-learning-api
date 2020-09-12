<template>
  <v-container class="movie-container" @click="openDialog">
    <movie-dialog ref="modal" :movie=selectedMovie />
    <v-card
      v-for="movie in movies"
      :key="movie.id"
      width="320px"
      min-height="400px"
      @click="selectedMovie = movie"
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
import MovieDialog from '~/components/MovieDialog.vue'
export default {
  components: {
    MovieDialog
  },
  data() {
    return {
      selectedMovie: {}
    }
  },
  props: {
    movies: {
      type: Array,
      default: () => {}
    }
  },
  methods: {
    openDialog() {
      this.$refs.modal.openDialog()
    }
  }
}
</script>

<style>
.movie-container {
  margin-top: 40px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: 40px;
}
</style>
