<template>
  <md-dialog :md-active.sync="dialogOpen" :md-click-outside-to-close="false">
    <!-- <form novalidate class="md-layout" @submit.prevent="validateContainer"> -->
    <md-dialog-title>Add Container</md-dialog-title>
    <md-dialog-content>
      <md-field :class="getValidationClass('name')">
        <label for="name">Name</label>
        <md-input type="text" name="name" id="name" v-model="form.name" />
        <span class="md-error" v-if="!$v.form.name.required"
          >Container name is required</span
        >
        <!-- <span class="md-error" v-else-if="!$v.form.name.email"
            >Invalid email</span
          > -->
      </md-field>

      <div class="md-layout md-gutter">
        <div class="md-layout-item md-large-size-33 md-medium-size-100">
          <md-field :class="getValidationClass('xAxis')">
            <label for="x-axis">X-Axis (cm)</label>
            <md-input
              type="number"
              name="x-axis"
              id="x-axis"
              v-model="form.xAxis"
            />
            <span class="md-error" v-if="!$v.form.xAxis.required"
              >X-Axis is required</span
            >
            <!-- <span class="md-error" v-else-if="!$v.form.xAxis.minlength"
                >Invalid X-Axis</span
              > -->
          </md-field>
        </div>

        <div class="md-layout-item md-large-size-33 md-medium-size-100">
          <md-field :class="getValidationClass('zAxis')">
            <label for="z-axis">Z-Axis (cm)</label>
            <md-input
              type="number"
              name="z-axis"
              id="z-axis"
              v-model="form.zAxis"
            />
            <span class="md-error" v-if="!$v.form.zAxis.required"
              >Z-Axis is required</span
            >
            <!-- <span class="md-error" v-else-if="!$v.form.zAxis.minlength"
                >Invalid Z-Axis</span
              > -->
          </md-field>
        </div>
        <!-- </div> -->

        <div class="md-layout-item md-large-size-33 md-medium-size-100">
          <md-field :class="getValidationClass('yAxis')">
            <label for="y-axis">Y-Axis (cm)</label>
            <md-input
              type="number"
              name="y-axis"
              id="y-axis"
              v-model="form.yAxis"
            />
            <span class="md-error" v-if="!$v.form.yAxis.required"
              >Y-Axis is required</span
            >
            <!-- <span class="md-error" v-else-if="!$v.form.yAxis.minlength"
                >Invalid Y-Axis</span
              > -->
          </md-field>
        </div>

        <div class="md-layout-item md-large-size-50 md-medium-size-100">
          <md-field :class="getValidationClass('weightLimit')">
            <label for="weight-limit">Weight Limit (kg)</label>
            <md-input
              type="number"
              name="weight-limit"
              id="weight-limit"
              v-model="form.weightLimit"
            />
            <span class="md-error" v-if="!$v.form.weightLimit.required"
              >Weight limit is required</span
            >
          </md-field>
        </div>

        <div class="md-layout-item md-large-size-50 md-medium-size-100">
          <md-field :class="getValidationClass('count')">
            <label for="count">Count</label>
            <md-input
              type="number"
              name="count"
              id="count"
              v-model="form.count"
            />
            <span class="md-error" v-if="!$v.form.count.required"
              >Count is required</span
            >
          </md-field>
        </div>
      </div>
      <!-- <span class="md-error" v-else-if="!$v.form.weightLimit.minlength"
                >Invalid weight limit</span
              > -->
      <!-- <span class="md-error" v-else-if="!$v.form.count.minlength"
                >Invalid count</span
              > -->
    </md-dialog-content>

    <md-dialog-actions>
      <md-button
        class="md-secondary"
        @click="fillWithDefault"
        style="position: absolute; left: 10px;"
        >Default</md-button
      >
      <md-button class="md-primary" @click="onClose">Cancel</md-button>
      <!-- <md-button class="md-primary" @click="onAdd('fuck')">Add</md-button> -->
      <md-button class="md-primary" type="submit" @click="validateContainer"
        >Add</md-button
      >
    </md-dialog-actions>
    <!-- </form> -->
  </md-dialog>
</template>

<script>
import { v4 as uuidv4 } from "uuid";
import { validationMixin } from "vuelidate";
import {
  required,
  // email,
  minLength,
  // maxLength,
} from "vuelidate/lib/validators";
export default {
  name: "AddContainer",
  mixins: [validationMixin],
  props: {
    dialogOpen: Boolean,
    onClose: Function,
    onAdd: Function,
  },
  data: () => ({
    form: {
      name: null,
      xAxis: null,
      yAxis: null,
      zAxis: null,
      weightLimit: null,
      count: null,
    },
  }),
  validations: {
    form: {
      name: {
        required,
        minLength: minLength(3),
      },
      xAxis: {
        required,
      },
      yAxis: {
        required,
      },
      zAxis: {
        required,
      },
      weightLimit: {
        required,
      },
      count: {
        required,
      },
    },
  },
  methods: {
    getValidationClass(fieldName) {
      const field = this.$v.form[fieldName];

      if (field) {
        return {
          "md-invalid": field.$invalid && field.$dirty,
        };
      }
    },
    clearForm() {
      this.$v.$reset();
      this.form.name = null;
      this.form.xAxis = null;
      this.form.yAxis = null;
      this.form.zAxis = null;
      this.form.weightLimit = null;
      this.form.count = null;
    },
    addContainer() {
      this.onAdd({
        ID: uuidv4(),
        TypeName: this.form.name,
        X: this.form.xAxis.toString(),
        Y: this.form.yAxis.toString(),
        Z: this.form.zAxis.toString(),
        Weight_limmit: this.form.weightLimit.toString(),
        Numbers: this.form.count.toString(),
      });
      this.clearForm();
    },
    fillWithDefault() {
      this.form = {
        ...this.form,
        name: "Default Container",
        xAxis: 227,
        yAxis: 225,
        zAxis: 580,
        weightLimit: 20000,
        count: 1,
      };
    },
    validateContainer() {
      this.$v.$touch();
      if (!this.$v.$invalid) {
        this.addContainer();
      }
    },
  },
};
</script>

<style scoped></style>
