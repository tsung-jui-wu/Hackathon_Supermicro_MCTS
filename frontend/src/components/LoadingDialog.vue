<template>
  <md-dialog :md-active.sync="dialogOpen" :md-click-outside-to-close="false">
    <!-- <form novalidate class="md-layout" @submit.prevent="validateBox"> -->
    <md-dialog-title>Loading ...</md-dialog-title>
    <md-dialog-content>
      <md-progress-spinner
        style="position: absolute; top: 50%; left: 50%;"
        md-mode="indeterminate"
      ></md-progress-spinner
    ></md-dialog-content>
    <!-- </form> -->
  </md-dialog>
</template>

<script></script>

<style scoped></style>
