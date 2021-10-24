<template>
  <div style="margin-left: 24px; margin-right: 24px;">
    <h2 style="margin-top: 32px;">Pallets</h2>

    <md-content class="md-layout md-gutter">
      <div
        class="md-layout-item md-large-size-50 md-medium-size-100"
        v-for="(pallet, index) in pallets"
        v-bind:key="pallet.ID + index.toString()"
      >
        <md-card
          md-with-hover
          style="margin-left: 0; margin-right: 0; margin-top: 16px; margin-bottom: 16px;"
        >
          <div class="md-layout md-row align-items-center">
            <img
              src="../../imgs/pallet.png"
              style="height: 120px; width: 120px; margin-left: 24px; margin-right: 12px;"
            />
            <div>
              <md-card-header>
                <div class="md-headline">{{ pallet.TypeName }}</div>
              </md-card-header>

              <md-card-content>
                <div class="md-subheading">{{ pallet.Numbers }} pallet(s)</div>
                <div class="md-body1">
                  {{ pallet.X }} x {{ pallet.Y }} x {{ pallet.Z }} (cm)
                </div>
                <div class="md-body1">{{ pallet.Weight }} (kg)</div>
              </md-card-content>

              <md-card-actions>
                <md-button
                  class="md-accent"
                  v-on:click="handleDeletePallet(pallet)"
                  >Delete</md-button
                >
              </md-card-actions>
            </div>
          </div>
        </md-card>
      </div>
    </md-content>

    <md-button class="md-fab md-primary" v-on:click="addPallet">
      <md-icon>add</md-icon>
    </md-button>
    <add-Pallet
      :dialogOpen="dialogOpen"
      :onAdd="handleAddPallet"
      :onClose="handleCloseDialog"
    />
  </div>
</template>

<script>
import AddPallet from "../components/AddPallet.vue";
export default {
  name: "Pallets",
  components: {
    AddPallet,
  },
  data: () => ({
    dialogOpen: false,
  }), //end Pallet_info //end data
  computed: {
    pallets() {
      return this.$store.getters.palletInfos;
    },
  }, //end computed
  methods: {
    addPallet() {
      this.dialogOpen = true;
    },
    handleAddPallet(pallet) {
      this.$store.dispatch("appendPalletInfos", [pallet]);
      this.dialogOpen = false;
      console.log(this.pallets);
    },
    handleCloseDialog() {
      this.dialogOpen = false;
    },
    handleDeletePallet(pallet) {
      this.$store.dispatch("deletePallet_infosItemWithUUID", pallet.ID);
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
