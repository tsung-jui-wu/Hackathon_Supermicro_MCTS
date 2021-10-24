<template>
  <div style="margin-left: 24px; margin-right: 24px;">
    <h2 style="margin-top: 32px;">Backups</h2>

    <md-content class="md-layout md-gutter">
      <div class="md-layout-item md-large-size-50 md-medium-size-100">
        <md-card
          md-with-hover
          style="margin-left: 0; margin-right: 0; margin-top: 16px; margin-bottom: 16px;"
        >
          <md-card-header>
            <div class="md-headline">Backup Configuration</div>
          </md-card-header>

          <md-card-content>
            <!-- <div class="md-subheading">
            </div> -->
            <div class="md-body1">
              Backup current configuration in JSON format.
            </div>
          </md-card-content>

          <md-card-actions>
            <md-button class="md-primary" v-on:click="downloadConfiguration"
              >Download</md-button
            >
          </md-card-actions>
        </md-card>
      </div>

      <div class="md-layout-item md-large-size-50 md-medium-size-100">
        <md-card
          md-with-hover
          style="margin-left: 0; margin-right: 0; margin-top: 16px; margin-bottom: 16px;"
        >
          <md-card-header>
            <div class="md-headline">Restore Configuration</div>
          </md-card-header>

          <md-card-content>
            <!-- <div class="md-subheading">
            </div> -->
            <div class="md-body1">
              Restore configuration from JSON file.
            </div>
          </md-card-content>

          <md-card-actions>
            <md-field>
              <label>Configuration JSON file</label>
              <md-file v-model="configFile" />
            </md-field>
            <md-button
              class="md-primary"
              style="margin-left: 12px;"
              v-on:click="uploadConfiguration"
              >Upload</md-button
            >
          </md-card-actions>
        </md-card>
      </div>
    </md-content>
  </div>
</template>

<script>
export default {
  data: () => ({
    configFile: "",
  }),
  methods: {
    downloadConfiguration() {
      var configuraton = {
        containerInfos: this.$store.getters.containerInfos,
        palletInfos: this.$store.getters.palletInfos,
        boxInfos: this.$store.getters.boxInfos,
      };
      this.saveFile(configuraton);
    },
    saveFile: function(obj) {
      const data = JSON.stringify(obj);
      const blob = new Blob([data], { type: "text/plain" });
      const e = document.createEvent("MouseEvents"),
        a = document.createElement("a");
      a.download = "test.json";
      a.href = window.URL.createObjectURL(blob);
      a.dataset.downloadurl = ["text/json", a.download, a.href].join(":");
      e.initEvent(
        "click",
        true,
        false,
        window,
        0,
        0,
        0,
        0,
        0,
        false,
        false,
        false,
        false,
        0,
        null
      );
      a.dispatchEvent(e);
    },
    uploadConfiguration() {
      // let reader = new FileReader();
      // reader.readAsText(this.configFile, "UTF-8");
      // reader.onload = (evt) => {
      //   let text = evt.target.result;
      //   try {
      //     var configuration = JSON.parse(text);
      //     console.log(configuration);
      //   } catch (e) {
      //     alert("Sorry, your file doesn't appear to be valid JSON data.");
      //   }
      // };
    },
  },
};
</script>

<style></style>
