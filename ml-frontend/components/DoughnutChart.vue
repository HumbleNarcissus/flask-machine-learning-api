<script>
import { Doughnut } from 'vue-chartjs'

export default {
  extends: Doughnut,
  props: {
    labels: {
      type: Array,
      default: () => []
    },
    datasets: {
      type: Array,
      default: () => []
    }
  },
  mounted() {
    this.renderChart({
      labels: this.labels,
      datasets: this.datasets
    })
  },
  watch: {
    datasets() {
      this.renderChart({
        labels: this.labels,
        datasets: this.datasets
      })
    }
  }
}
</script>
