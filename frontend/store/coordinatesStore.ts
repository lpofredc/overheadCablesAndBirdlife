/**
 * Nuxt Point module: coordinatesStore to handle creation of new Point
 */

import { defineStore } from "pinia";
import { Interface } from "readline";

export const useCoordinatesStore = defineStore("coordinates", {
  state: () => ({
    newPointCoord: {} as NewPointCoord,
    newLineCoord: [],
  }),
  getters: {
    /**
     * Getter for newPointCoord state values
     *
     * @param {state} state of this store module
     * @return {JSON object} object with latitude and longitude data
     */
    getNewPointCoord(state) {
      return state.newPointCoord;
    },
    /**
     * Getter for newLineCoord state values
     *
     * @param {state} state of this store module
     * @return {JSON object} object with Line coordinates data (latitude and longitude)
     */
    getNewLineCoord(state) {
      return state.newLineCoord;
    },
  },
  actions: {
    setNewPointCoord(data: NewPointCoord) {
      this.newPointCoord = data;
    },
    setNewLineCoord(data: []) {
      this.newLineCoord = data;
    },
  },
});

interface NewPointCoord {
  lat: number | null;
  lng: number | null;
  default?: null;
}
