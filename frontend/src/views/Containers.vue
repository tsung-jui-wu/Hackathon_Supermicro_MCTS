<template>
  <div style="margin-left: 24px; margin-right: 24px;">
    <h2 style="margin-top: 32px;">Containers</h2>

    <md-content class="md-layout md-gutter">
      <div
        class="md-layout-item md-large-size-50 md-medium-size-100"
        v-for="(container, index) in containers"
        v-bind:key="container.ID + index.toString()"
      >
        <md-card
          md-with-hover
          style="margin-left: 0; margin-right: 0; margin-top: 16px; margin-bottom: 16px;"
        >
          <div class="md-layout md-row align-items-center">
            <img
              src="../../imgs/container.png"
              style="height: 120px; width: 120px; margin-left: 24px; margin-right: 12px;"
            />
            <div>
              <md-card-header>
                <div class="md-headline">{{ container.TypeName }}</div>
              </md-card-header>

              <md-card-content>
                <div class="md-subheading">
                  {{ container.Numbers }} container(s)
                </div>
                <div class="md-body1">
                  {{ container.X }} x {{ container.Y }} x {{ container.Z }} (cm)
                </div>
                <div class="md-body1">
                  Weight Limit: {{ container.Weight_limmit }} (kg)
                </div>
              </md-card-content>

              <md-card-actions>
                <md-button
                  class="md-accent"
                  v-on:click="handleDeleteContainer(container)"
                  >Delete</md-button
                >
              </md-card-actions>
            </div>
          </div>
        </md-card>
      </div>
    </md-content>

    <md-button class="md-fab md-primary" v-on:click="addContainer">
      <md-icon>add</md-icon>
    </md-button>
    <add-container
      :dialogOpen="dialogOpen"
      :onAdd="handleAddContainer"
      :onClose="handleCloseDialog"
    />
  </div>
</template>

<script>
import AddContainer from "../components/AddContainer.vue";
export default {
  name: "Containers",
  components: {
    AddContainer,
  },
  data: () => ({
    dialogOpen: false,
  }), //end container_info //end data
  computed: {
    containers() {
      return this.$store.getters.containerInfos;
    },
  }, //end computed
  methods: {
    addContainer() {
      this.dialogOpen = true;
    },
    handleAddContainer(container) {
      this.$store.dispatch("appendContainerInfos", [container]);
      this.dialogOpen = false;
    },
    handleCloseDialog() {
      this.dialogOpen = false;
    },
    handleDeleteContainer(container) {
      this.$store.dispatch("deleteContainer_infosItemWithUUID", container.ID);
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
