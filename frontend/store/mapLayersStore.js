/**
 * mapLayerStore to handle map layers loading
 */
export const state = () => ({
  baseLayers: [],
})

export const mutations = {
  /**
   * Mutation: apply baseLayers value change to state of current store module
   *
   * "baseLayers" contains URLs to Web Map Tile Service
   *
   * @param {state} state of this store module
   * @param {JSON object} contains object containing information for map layer loading
   */
  addBaseLayers(state, data) {
    state.baseLayers = data
  },
}

export const getters = {
  /**
   * Getter for baseLayers state value
   *
   * @param {state} state of this store module
   * @return {JSON object} object containing information for map layer loading
   */
  baseLayers(state) {
    return state.baseLayers
  },
}

export const actions = {
  async loadBaseLayers({ commit }) {
    try {
      // gather layers from DB to be loaded with map
      const data = await this.$axios.$get('map-layers/baselayers/')
      if (data === undefined) {
        throw new Error('conditions')
      }
      commit('addBaseLayers', data)
    } catch (err) {
      console.error('ERROR', err)
      const error = {}
      if (err.toString().includes('404')) {
        error.code = errorCodes.nomenclature_not_found.code
        error.msg = $nuxt.$t(`error.${errorCodes.nomenclature_not_found.msg}`)
        // if nuxt error message contains substring 'conditions'
      }
      commit('errorStore/setError', error, { root: true })
      // log out user as application may not be reliable as is
      $nuxt.$auth.logout()
    }
  },
}
