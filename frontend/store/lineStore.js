/** Nuxt Line module: lineStore to handle creation of new Line */

import { defineStore } from 'pinia'

export const useLineStore = defineStore('lines', {
  state: () => ({ newLineCoord: [] }),
  getters: {
    /**
     * Getter for newPointCoord state values
     *
     * @param {state} state of this store module
     * @return {JSON object} object with latitude and longitude data
     */
    newLineCoord (state) {
      return state.newLineCoord
    }
  }
})
