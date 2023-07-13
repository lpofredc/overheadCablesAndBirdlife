/**
 * mapLayerStore to handle map layers loading
 */

import { defineStore } from "pinia";
import { GeoJSON, FeatureCollection } from "geojson";

export const useMortalityStore = defineStore("mortality", {
  state: () => ({ mortalityData: {} as FeatureCollection }),
  getters: {
    // // get FeatureCollection data
    // infstrData(state) {
    //   return state.infstrData
    // },
    // get FeatureCollection array containing data (Json Object)
    getMortalityFeatures(state) {
      return state.mortalityData.features;
    },
  },
  actions: {
    async getMortalityData() {
      await $fetch("/api/v1/mortality/")
        .then((data) => {
          this.mortalityData = data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
});

interface MortalityData {
  properties: {
    id: number;
    vernacular_name: string;
    scientific_name: string;
    death_cause?: string;
    default: boolean | undefined;
  };
}
