<template>
  <div class="page-container" id="app">
    <md-app>
      <md-app-toolbar class="md-primary" md-elevation="0">
        <md-button
          class="md-icon-button"
          @click="toggleMenu"
          v-if="!menuVisible"
        >
          <md-icon>menu</md-icon>
        </md-button>
        <span class="md-title">3D-Bin Packing</span>
      </md-app-toolbar>

      <md-app-drawer :md-active.sync="menuVisible" md-persistent="mini">
        <md-toolbar class="md-transparent" md-elevation="0">
          <span>Options</span>

          <div class="md-toolbar-section-end">
            <md-button class="md-icon-button md-dense" @click="toggleMenu">
              <md-icon>keyboard_arrow_left</md-icon>
            </md-button>
          </div>
        </md-toolbar>

        <md-list>
          <md-list-item to="/containers">
            <md-icon>archive</md-icon>
            <span class="md-list-item-text">Containers</span>
          </md-list-item>

          <md-list-item to="/pallets">
            <md-icon>view_stream</md-icon>
            <span class="md-list-item-text">Pallets</span>
          </md-list-item>

          <md-list-item to="/boxes">
            <md-icon>inventory_2</md-icon>
            <span class="md-list-item-text">Boxes</span>
          </md-list-item>

          <md-list-item to="/render">
            <md-icon>play_arrow</md-icon>
            <span class="md-list-item-text">Render</span>
          </md-list-item>

          <md-list-item to="/rendernew">
            <md-icon>play_arrow</md-icon>
            <span class="md-list-item-text">Render (New)</span>
          </md-list-item>

          <md-list-item to="/backups">
            <md-icon>backup</md-icon>
            <span class="md-list-item-text">Backups</span>
          </md-list-item>
        </md-list>
      </md-app-drawer>
      <md-app-content>
        <router-view />
      </md-app-content>
    </md-app>
    <!-- <div id="app">
    <div id="nav">
      <custom-navbar/>
    </div>
    <router-view/>
  </div> -->
  </div>
</template>

<script>
// import CustomNavbar from './components/CustomNavbar.vue'
export default {
  name: "App",
  components: {
    // CustomNavbar,
  },
  data: () => ({
    menuVisible: true,
  }),
  methods: {
    toggleMenu() {
      this.menuVisible = !this.menuVisible;
    },
  },
};
</script>
<style scoped>
.md-app {
  min-height: 500px;
  height: 100vh;
  border: 1px solid rgba(#000, 0.12);
}

.md-drawer {
  width: 230px;
  max-width: calc(100vw - 125px);
}
</style>
