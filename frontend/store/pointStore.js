/** Nuxt Point module: pointStore to handle creation of new Point */
export const state = () => ({
  newLat: { type: Number, default: null },
  newLng: { type: Number, default: null },
  newPointCoord: {
    lat: { type: Number, default: null },
    lng: { type: Number, default: null },
    default: null,
  },
  // pointGeoJson: {
  //   type: 'Feature',
  //   properties: { id: 1, test: 'test' },
  //   geometry: {
  //     type: 'Point',
  //     coordinates: [null, null],
  //   },
  // },
})

export const mutations = {
  // addGeoJson(state, data) {
  //   state.pointGeoJson = data
  //   state.newLat = data.geometry.coordinates[0]
  //   state.newLng = data.geometry.coordinates[1]
  //   state.newPointCoord = {
  //     lng: data.geometry.coordinates[0],
  //     lat: data.geometry.coordinates[1],
  //   }
  // },
  /**
   * Mutation: apply newPointCoord value change to state of current store module
   *
   * @param {state} state of this store module
   * @param {JSON object} contains object with latitude and longitude data
   */
  add(state, data) {
    state.newPointCoord = data
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
  // pointGeoJson(state) {
  //   return state.pointGeoJson
  // },
  /**
   * Getter for newPointCoord state values
   *
   * @param {state} state of this store module
   * @return {JSON object} object with latitude and longitude data
   */
  newPointCoord(state) {
    return state.newPointCoord
  },
  /**
   * Getter for newPointCoord state values
   *
   * @param {state} state of this store module
   * @return {Number} latitude coordinate
   */
  newLat(state) {
    return state.newLat
  },
  /**
   * Getter for newPointCoord state values
   *
   * @param {state} state of this store module
   * @return {Number} longitude coordinate
   */
  newLng(state) {
    return state.newLng
  },
}

/** ##############################################################################################
 *  #####################     OLD VERSION     ####################################################
 *  ##############################################################################################
 */

// /** Nuxt Point module: pointStore to handle creation of new Point */
// export const state = () => ({
//   newLat: { type: Number, default: null },
//   newLng: { type: Number, default: null },
//   newPointCoord: {
//     lat: { type: Number, default: null },
//     lng: { type: Number, default: null },
//     default: null,
//   },
// })

// export const mutations = {
//   /**
//    * Mutation: apply newPointCoord value change to state of current store module
//    *
//    * @param {state} state of this store module
//    * @param {JSON object} contains object with latitude and longitude data
//    */
//   add(state, data) {
//     state.newPointCoord = data
//   },
//   // USELESS FOR NOW
//   // /**
//   //  * Mutation: apply newLat value change to state of current store module
//   //  *
//   //  * @param {state} state of this store module
//   //  * @param {Number} contains Latitude coordinate
//   //  */
//   // addLat(state, data) {
//   //   state.newLat = data
//   // },
//   // /**
//   //  * Mutation: apply newLng value change to state of current store module
//   //  */** Nuxt Point module: pointStore to handle creation of new Point */
// export const state = () => ({
//   newLat: { type: Number, default: null },
//   newLng: { type: Number, default: null },
//   newPointCoord: {
//     lat: { type: Number, default: null },
//     lng: { type: Number, default: null },
//     default: null,
//   },
// })

// export const mutations = {
//   /**
//    * Mutation: apply newPointCoord value change to state of current store module
//    *
//    * @param {state} state of this store module
//    * @param {JSON object} contains object with latitude and longitude data
//    */
//   add(state, data) {
//     state.newPointCoord = data
//   },
//   // USELESS FOR NOW
//   // /**
//   //  * Mutation: apply newLat value change to state of current store module
//   //  *
//   //  * @param {state} state of this store module
//   //  * @param {Number} contains Latitude coordinate
//   //  */
//   // addLat(state, data) {
//   //   state.newLat = data
//   // },
//   // /**
//   //  * Mutation: apply newLng value change to state of current store module
//   //  *
//   //  * @param {state} state of this store module
//   //  * @param {Number} contains Longitude coordinate
//   //  */
//   // addLng(state, data) {
//   //   state.newLng = data
//   // },
// }

// export const getters = {
//   /**
//    * Getter for newPointCoord state values
//    *
//    * @param {state} state of this store module
//    * @return {JSON object} object with latitude and longitude data
//    */
//   newPointCoord(state) {
//     return state.newPointCoord
//   },
//   /**
//    * Getter for newPointCoord state values
//    *
//    * @param {state} state of this store module
//    * @return {Number} latitude coordinate
//    */
//   newLat(state) {
//     return state.newLat
//   },
//   /**
//    * Getter for newPointCoord state values
//    *
//    * @param {state} state of this store module
//    * @return {Number} longitude coordinate
//    */
//   newLng(state) {
//     return state.newLng
//   },
// }

//   //  * @param {state} state of this store module
//   //  * @param {Number} contains Longitude coordinate
//   //  */
//   // addLng(state, data) {
//   //   state.newLng = data
//   // },
// }

// export const getters = {
//   /**
//    * Getter for newPointCoord state values
//    *
//    * @param {state} state of this store module
//    * @return {JSON object} object with latitude and longitude data
//    */
//   newPointCoord(state) {
//     return state.newPointCoord
//   },
//   /**
//    * Getter for newPointCoord state values
//    *
//    * @param {state} state of this store module
//    * @return {Number} latitude coordinate
//    */
//   newLat(state) {
//     return state.newLat
//   },
//   /**
//    * Getter for newPointCoord state values
//    *
//    * @param {state} state of this store module
//    * @return {Number} longitude coordinate
//    */
//   newLng(state) {
//     return state.newLng
//   },
// }
