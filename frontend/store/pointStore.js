/** Nuxt Point module: pointStore to handle creation of new Point */
export const state = () => ({
  newLat: null,
  newLng: null,
  newCoord: null,
})

export const mutations = {
  /**
   * Mutation: apply newCoord value change to state of current store module
   *
   * @param {state} state of this store module
   * @param {JSON object} contains object with latitude and longitude data
   */
  add(state, data) {
    state.newCoord = data
  },
  // USELESS FOR NOW
  // /**
  //  * Mutation: apply newLat value change to state of current store module
  //  *
  //  * @param {state} state of this store module
  //  * @param {Number} contains Latitude coordinate
  //  */
  // addLat(state, data) {
  //   state.newLat = data
  // },
  // /**
  //  * Mutation: apply newLng value change to state of current store module
  //  *
  //  * @param {state} state of this store module
  //  * @param {Number} contains Longitude coordinate
  //  */
  // addLng(state, data) {
  //   state.newLng = data
  // },
}

export const getters = {
  /**
   * Getter for newCoord state values
   *
   * @param {state} state of this store module
   * @return {JSON object} object with latitude and longitude data
   */
  newCoord(state) {
    return state.newCoord
  },
  /**
   * Getter for newCoord state values
   *
   * @param {state} state of this store module
   * @return {Number} latitude coordinate
   */
  newLat(state) {
    return state.newLat
  },
  /**
   * Getter for newCoord state values
   *
   * @param {state} state of this store module
   * @return {Number} longitude coordinate
   */
  newLng(state) {
    return state.newLng
  },
}
