export const state = () => ({
  movies: []
})

export const mutations = {
  GET_MOVIES: (state, movies) => {
    state.movies = movies
  },
  POST_MOVIE: (state, movie) => {
    state.movies = [
      ...state.movies,
      movie
    ]
  }
}

export const actions = {
  async getMovies({ commit }) {
    try {
      const { movies } = await this.$axios.$get('/prediction')
      commit('GET_MOVIES', movies)
    } catch (error) {
      this.$toast.error('GET movies error.')
    }
  },
  async postMovie({ commit }, data) {
    try {
      const { result } = await this.$axios.$post('/prediction', data)
      commit('POST_MOVIE', result)
    } catch (error) {
      this.$toast.error('Error while adding new movie.')
    }
  }
}