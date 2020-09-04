<template>
  <div class="text-center">
    <v-dialog v-model="dialog" width="500">
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="blue" v-bind="attrs" v-on="on">
          Add new movie
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="headline blue">
          Add new movie data
        </v-card-title>

        <v-container>
          <v-form v-model="valid">
            <v-text-field
              v-model="data.title"
              :rules="requiredRules"
              label="Movie Title"
              required
            ></v-text-field>
            <v-text-field
              v-model="data.url"
              :rules="requiredRules"
              label="Movie image url"
              required
            ></v-text-field>
            <div
              v-for="(input, index) in data.inputs"
              :key="index"
              class="mb-3 mt-4"
            >
              <v-textarea
                v-model="input.name"
                label="Comment text"
                hide-details
                auto-grow
                outlined
                required
              ></v-textarea>
              <div class="d-flex justify-end mt-4">
                <v-btn
                  color="green"
                  @click="addInput()"
                  v-show="index === data.inputs.length - 1"
                  class="mr-2"
                >
                  Add
                </v-btn>
                <v-btn color="red" @click="deleteInput(index)">
                  Delete
                </v-btn>
              </div>
            </div>
          </v-form>
        </v-container>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="dialog = false">
            Submit
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dialog: false,
      valid: false,
      requiredRules: [v => !!v || "Field is required"],
      data: {
        title: "",
        url: "",
        inputs: [{ text: "" }]
      }
    };
  },
  methods: {
    addInput() {
      this.data.inputs.push({ text: "" });
    },
    deleteInput(index) {
      this.data.inputs.splice(index, 1);
    }
  }
};
</script>
