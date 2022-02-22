/** Nuxt Point module: pointStore to handle Point data changes */
export /**
 * newCoord is an object containing Latiture and Longitude data.
 *
 * example: {lat: 0.15478, lng: 3.6958}
 */
const state = () => ({
  newCoord: null,
})

export const mutations = {
  /**
   * Mutation: apply value change to state of current store module
   *
   * @param {state} state of this store module
   * @param {geoJson object} contains new LMarker object
   */
  add(state, data) {
    state.newCoord = data
  },
}

export const getters = {
  /**
   * Getter for Sensitive Area data as geoJson object
   *
   * @param {state} state of this store module
   * @return {LMarker} new LMarker object
   */
  newCoord(state) {
    return state.newCoord
  },
}
