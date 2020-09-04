<template>
  <div>
    <v-app-bar dense dark>
      <v-toolbar-title>ML comment checker</v-toolbar-title>
      <v-spacer />
      <Dialog />
    </v-app-bar>
  </div>
</template>

</template>

<script>
import Dialog from '~/components/Dialog.vue'
export default {
  components: { Dialog }
}
</script>

<style>

</style>