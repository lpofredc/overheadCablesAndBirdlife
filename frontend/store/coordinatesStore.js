/**
 * Nuxt Point module: coordinatesStore to handle creation of new Point
 */

import { defineStore } from 'pinia'

export const useCoordinatesStore = defineStore('coordinates', {
  state: () => ({
    lat: { type: Number, default: null },
    lng: { type: Number, default: null },
    default: null
  }),
  getters: {
    /**
     * Getter for newPointCoord state values
     *
     * @param {state} state of this store module
     * @return {JSON object} object with latitude and longitude data
     */
    newPointCoord (state) {
      return state.newPointCoord
    },
    /**
     * Getter for newLineCoord state values
     *
     * @param {state} state of this store module
     * @return {JSON object} object with Line coordinates data (latitude and longitude)
     */
    newLineCoord (state) {
      return state.newLineCoord
    }
  }
})
