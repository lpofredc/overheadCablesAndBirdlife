/** Nuxt Store module: errorStore module use to handle error message dispaly in snackbar */
export const state = () => ({
  // boolean value that toggle to trigger display of error message. Value has no role. Only the
  // value change trigger the action capture in watcher.
  isError: { type: Boolean, default: false },
  // Error message content
  err: {
    code: { type: Number, default: null },
    msg: { type: String, default: null },
  },
})

export const mutations = {
  toggle(state) {
    state.isError = !state.isError
  },
  setError(state, data) {
    state.err = data
  },
}

/**
 * Getter for isError level nomenclature items.
 *
 * @param {state} state of this store module
 * @return {JSON object} returns the list of nomenclature items for risk levels
 */
export const getters = {
  isError(state) {
    return state.isError
  },
  err(state) {
    return state.err
  },
}
