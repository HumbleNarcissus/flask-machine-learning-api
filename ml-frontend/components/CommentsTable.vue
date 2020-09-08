<template>
  <v-data-table
    :headers="headers"
    :items="comments"
    :items-per-page="10"
  ></v-data-table>
</template>

<script>
export default {
  props: {
    comments: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      headers: [
          { text: "Text", value: "text"},
          { text: "Probability", value: "prob" },
          { text: "Result", value: "positive" }
      ]
    };
  }
};
</script>

<style></style>
