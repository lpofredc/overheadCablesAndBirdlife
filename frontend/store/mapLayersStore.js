export const state = () => ({
  baseLayers: [],
})

export const mutations = {
  addBaseLayers(state, data) {
    state.baseLayers = data
  },
}

export const getters = {
  baseLayers(state) {
    return state.baseLayers
  },
}

export const actions = {
  async loadBaseLayers({ commit }) {
    try {
      const data = await this.$axios.$get('map-layers/baselayers/')
      if (data === undefined) {
        throw new Error('conditions')
      }
      commit('addBaseLayers', data)
      console.log('state.baseLayers', state.baseLayers)
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
