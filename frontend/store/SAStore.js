// Nuxt Store module: SAStore for Sensible Area module
export const state = () => ({
  SAData: {}, // Sensible Area data
})

export const mutations = {
  add(state, data) {
    state.SAData = data
  },
}

export const getters = {
  // get FeatureCollection data
  SAData(state) {
    return state.SAData
  },
  // get FeatureCollection array containing data (Json Object)
  SADataFeatures(state) {
    return state.SAData.features
  },
}
