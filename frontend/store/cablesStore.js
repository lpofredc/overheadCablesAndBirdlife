// Nuxt Store module: cablesStore for Cables module
export const state = () => ({
  infstrData: {}, // Infrastructure data
  pointData: {}, // Pole and Pylon data
  lineData: {}, // Cable lines data
  opData: [],
  pointOpData: [],
  LineOpData: [],
})

export const mutations = {
  add(state, data) {
    state.infstrData = data
    // gather Point and Line from fetched infrastructure data
    state.pointData = JSON.parse(JSON.stringify(data)) // deep copy of data Json Object
    // filter Point objects in data.features and set filtered array to "state.pointData.features"
    state.pointData.features = state.pointData.features.filter(
      (elem) => elem.resourcetype === 'Point'
    )
    state.lineData = JSON.parse(JSON.stringify(data)) // deep copy of data Json Object
    // filter Line objects in data.features and set filtered array to "state.lineData.features"
    state.lineData.features = state.lineData.features.filter(
      (elem) => elem.resourcetype === 'Line'
    )
  },
  addOperation(state, data) {
    state.opData = data.all
    state.pointOpData = data.point
    state.lineOpData = data.line
  },
}

export const getters = {
  // // get FeatureCollection data
  // infstrData(state) {
  //   return state.infstrData
  // },
  // get FeatureCollection array containing data (Json Object)
  infstrDataFeatures(state) {
    return state.infstrData.features
  },
  // pointData(state) {
  //   return state.pointData
  // },
  pointDataFeatures(state) {
    return state.pointData.features
  },
  // lineData(state) {
  //   return state.lineData
  // },
  lineDataFeatures(state) {
    return state.lineData.features
  },
  opData(state) {
    return state.opData
  },
  pointOpData(state) {
    return state.pointOpData
  },
  lineOpData(state) {
    return state.lineOpData
  },
}