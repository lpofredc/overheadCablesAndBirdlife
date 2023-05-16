// Nuxt Store module: cablesStore for Cables module
import { defineStore } from "pinia";

export const useCablesStore = defineStore("cables", {
  state: () => ({
    infstrData: {}, // Infrastructure data
    pointData: {}, // Pole and Pylon data
    lineData: {}, // Cable lines data
    opData: [],
    pointOpData: [],
    lineOpData: [],
  }),
  getters: {
    // // get FeatureCollection data
    // infstrData(state) {
    //   return state.infstrData
    // },
    // get FeatureCollection array containing data (Json Object)
    infstrDataFeatures(state) {
      return state.infstrData.features;
    },
    // pointData(state) {
    //   return state.pointData
    // },
    pointDataFeatures(state) {
      return state.pointData.features;
    },
    // lineData(state) {
    //   return state.lineData
    // },
    lineDataFeatures(state) {
      return state.lineData.features;
    },
    opData(state) {
      return state.opData;
    },
    pointOpData(state) {
      return state.pointOpData;
    },
    lineOpData(state) {
      return state.lineOpData;
    },
  },
  actions: {
    add(data) {
      this.infstrData = data;
      // gather Point and Line from fetched infrastructure data
      this.pointData = JSON.parse(JSON.stringify(data)); // deep copy of data Json Object
      // filter Point objects in data.features and set filtered array to "state.pointData.features"
      this.pointData.features = this.pointData.features.filter(
        (elem) => elem.resourcetype === "Point"
      );
      this.lineData = JSON.parse(JSON.stringify(data)); // deep copy of data Json Object
      // filter Line objects in data.features and set filtered array to "state.lineData.features"
      this.lineData.features = this.lineData.features.filter(
        (elem) => elem.resourcetype === "Line"
      );
    },
    addOperation(data) {
      this.opData = data.all;
      this.pointOpData = data.point;
      this.lineOpData = data.line;
    },
  },
});
