<template>
  <md-dialog :md-active.sync="dialogOpen" :md-click-outside-to-close="false">
    <!-- <form novalidate class="md-layout" @submit.prevent="validateBox"> -->
    <md-dialog-title>Add Box</md-dialog-title>
    <md-dialog-content>
      <md-field :class="getValidationClass('name')">
        <label for="name">Name</label>
        <md-input type="text" name="name" id="name" v-model="form.name" />
        <span class="md-error" v-if="!$v.form.name.required"
          >Box name is required</span
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

        <!-- <div class="md-layout md-gutter"> -->
        <div class="md-layout-item md-large-size-50 md-medium-size-100">
          <md-field :class="getValidationClass('weight')">
            <label for="weight-limit">Weight (kg)</label>
            <md-input
              type="number"
              name="weight-limit"
              id="weight-limit"
              v-model="form.weight"
            />
            <span class="md-error" v-if="!$v.form.weight.required"
              >Weight is required</span
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
      <!-- <span class="md-error" v-else-if="!$v.form.weight.minlength"
                >Invalid weight limit</span
              > -->
      <!-- <span class="md-error" v-else-if="!$v.form.count.minlength"
                >Invalid count</span
              > -->
    </md-dialog-content>

    <md-dialog-actions>
      <md-button
        class="md-secondary"
        @click="generateRandom"
        style="position: absolute; left: 10px;"
        >Random</md-button
      >
      <md-button class="md-primary" @click="onClose">Cancel</md-button>
      <!-- <md-button class="md-primary" @click="onAdd('fuck')">Add</md-button> -->
      <md-button class="md-primary" type="submit" @click="validateBox"
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
  name: "AddBox",
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
      weight: null,
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
      weight: {
        required,
      },
      count: {
        required,
      },
    },
  },
  methods: {
    randomLength() {
      return Math.round(Math.random() * (50 - 10) + 10);
    },
    randomWeight() {
      return Math.round(Math.random() * (50 - 10) + 10);
    },
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
      this.form.weight = null;
      this.form.count = null;
    },
    addBox() {
      this.onAdd({
        ID: uuidv4(),
        TypeName: this.form.name,
        X: this.form.xAxis.toString(),
        Y: this.form.yAxis.toString(),
        Z: this.form.zAxis.toString(),
        Weight: this.form.weight.toString(),
        Numbers: this.form.count.toString(),
      });
      this.clearForm();
    },
    generateRandom() {
      this.form = {
        ...this.form,
        name: "Random Box",
        xAxis: this.randomLength(),
        yAxis: this.randomLength(),
        zAxis: this.randomLength(),
        weight: this.randomWeight(),
        count: 1,
      };
    },
    validateBox() {
      this.$v.$touch();
      if (!this.$v.$invalid) {
        this.addBox();
      }
    },
  },
};
</script>

<style scoped></style>
