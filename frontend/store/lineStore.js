/** Nuxt Line module: lineStore to handle creation of new Line */
export const state = () => ({
  // newLat: null,
  // newLng: null,
  newLineCoord: [],
})

export const mutations = {
  /**
   * Mutation: apply newLineCoord value change to state of current store module
   *
   * @param {state} state of this store module
   * @param {JSON object[]} contains array of objects with latitude and longitude data matching to
   * Line coordinates
   */
  add(state, data) {
    state.newPointCoord = data
  },
}

export const getters = {
  /**
   * Getter for newPointCoord state values
   *
   * @param {state} state of this store module
   * @return {JSON object} object with latitude and longitude data
   */
  newLineCoord(state) {
    return state.newLineCoord
  },
  // /**
  //  * Getter for newPointCoord state values
  //  *
  //  * @param {state} state of this store module
  //  * @return {Number} latitude coordinate
  //  */
  // newLat(state) {
  //   return state.newLat
  // },
  // /**
  //  * Getter for newPointCoord state values
  //  *
  //  * @param {state} state of this store module
  //  * @return {Number} longitude coordinate
  //  */
  // newLng(state) {
  //   return state.newLng
  // },
}
