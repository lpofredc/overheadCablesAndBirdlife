/**
 * mapLayerStore to handle map layers loading
 */

import { defineStore } from "pinia";

export const useMapLayersStore = defineStore("mapLayers", {
  state: () => ({ baseLayers: [] }),
  getters: {
    baseLayers(state) {
      return state.baseLayers;
    },
  },
  actions: {
    async loadBaseLayers() {
      try {
        // gather layers from DB to be loaded with map
        const { data, error } = await useFetch(
          "http://localhost:8000/api/v1/map-layers/baselayers/"
        );
        this.baseLayers = data;
        console.log("DATA", data);
        if (error) {
          console.error("ERROR", error);
        }
      } catch (err) {
        console.error("ERROR err", err);
        const error = {};
        if (err.toString().includes("404")) {
          error.code = errorCodes.nomenclature_not_found.code;
          error.msg = $nuxt.$t(
            `error.${errorCodes.nomenclature_not_found.msg}`
          );
          // if nuxt error message contains substring 'conditions'
        }
        // commit("errorStore/setError", error, { root: true });
        // log out user as application may not be reliable as is
        // $nuxt.$auth.logout();
      }
    },
  },
});
