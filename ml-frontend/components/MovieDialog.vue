<template>
  <v-dialog class="movie-dialog" v-model="dialog" max-width="800">
    <v-card>
      <v-card-title>{{ movie.title }}</v-card-title>
      <comments-table :comments="movie.comments" />
      <doughnut-chart
        :labels="['Positive', 'Negative']"
        :datasets="createDataSets()"
      />
    </v-card>
  </v-dialog>
</template>

<script>
import CommentsTable from "~/components/CommentsTable.vue";
import DoughnutChart from "~/components/DoughnutChart.vue";
export default {
  compontenst: {
    CommentsTable,
    DoughnutChart
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
    };
  },
  methods: {
    openDialog() {
      this.dialog = true;
    },
    createDataSets() {
      const { comments = [] } = this.movie;
      const positive = comments.filter(item => item.positive === "Positive");
      const negative = comments.filter(item => item.positive === "Negative");
      return [{ data: [positive.length, negative.length], backgroundColor: ['green', 'red'] }];
    }
  }
};
</script>

<style></style>
