<template>
  <v-dialog class="movie-dialog" v-model="dialog" max-width="800">
    <v-card>
      <v-card-title>{{ movie.title }}</v-card-title>
      <comments-table :comments="movie.comments" />
    </v-card>
  </v-dialog>
</template>

<script>
import CommentsTable from '~/components/CommentsTable.vue'
export default {
  compontenst: {
    CommentsTable
  },
  props: {
    movie: {
      type: Object,
      default: () => {}
    }
  },
  data() {
    return {
      dialog: false
    }
  },
  methods: {
    openDialog() {
      this.dialog = true
    }
  }
};
</script>

<style></style>
