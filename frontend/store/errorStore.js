/** Nuxt Store module: errorStore module use to handle error message dispaly in snackbar */
export const state = () => ({
  // Error message content: The error message is set to "err". this listened by watcher that
  // triggers the display of message in snackbar (refer error-snackbar component)
  err: {
    code: { type: Number, default: null },
    msg: { type: String, default: null },
  },
})

/**
 * mutations are used to change state value from errorStore
 */
export const mutations = {
  setError(state, data) {
    state.err = data
  },
}

/**
 * Getter for state value "err" level nomenclature items.
 *
 * @param {state} state of this store module
 * @return {JSON object} returns the "err" object
 */
export const getters = {
  err(state) {
    return state.err
  },
}
