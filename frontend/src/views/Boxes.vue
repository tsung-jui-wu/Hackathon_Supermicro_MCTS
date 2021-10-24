<template>
  <div style="margin-left: 24px; margin-right: 24px;">
    <h2 style="margin-top: 32px;">Boxes</h2>

    <md-content class="md-layout md-gutter">
      <div
        class="md-layout-item md-large-size-50 md-medium-size-100"
        v-for="(box, index) in boxes"
        v-bind:key="box.ID + index.toString()"
      >
        <md-card
          md-with-hover
          style="margin-left: 0; margin-right: 0; margin-top: 16px; margin-bottom: 16px;"
        >
          <div class="md-layout md-row align-items-center">
            <img
              src="../../imgs/box.png"
              style="height: 120px; width: 120px; margin-left: 24px; margin-right: 12px;"
            />
            <div>
              <md-card-header>
                <div class="md-headline">{{ box.TypeName }}</div>
              </md-card-header>

              <md-card-content>
                <div class="md-subheading">{{ box.Numbers }} box(es)</div>
                <div class="md-body1">
                  {{ box.X }} x {{ box.Y }} x {{ box.Z }} (cm)
                </div>
                <div class="md-body1">{{ box.Weight }} (kg)</div>
              </md-card-content>

              <md-card-actions>
                <md-button class="md-accent" v-on:click="handleDeleteBox(box)"
                  >Delete</md-button
                >
              </md-card-actions>
            </div>
          </div>
        </md-card>
      </div>
    </md-content>

    <md-button class="md-fab md-primary" v-on:click="addBox">
      <md-icon>add</md-icon>
    </md-button>
    <add-box
      :dialogOpen="dialogOpen"
      :onAdd="handleAddBox"
      :onClose="handleCloseDialog"
    />
  </div>
</template>

<script>
import AddBox from "../components/AddBox.vue";
export default {
  name: "Boxes",
  components: {
    AddBox,
  },
  data: () => ({
    dialogOpen: false,
  }), //end box_info //end data
  computed: {
    boxes() {
      return this.$store.getters.boxInfos;
    },
  }, //end computed
  methods: {
    addBox() {
      this.dialogOpen = true;
    },
    handleAddBox(box) {
      this.$store.dispatch("appendBoxInfos", [box]);
      this.dialogOpen = false;
    },
    handleCloseDialog() {
      this.dialogOpen = false;
    },
    handleDeleteBox(box) {
      this.$store.dispatch("deleteBox_infosItemWithUUID", box.ID);
    },
  }, //end methods
};
</script>

<style scoped>
.md-button {
  position: absolute;
  bottom: 24px;
  right: 24px;
}

/* .img {
  height: 100px;
  width: 100px;
} */
</style>
