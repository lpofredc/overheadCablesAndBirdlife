/** Nuxt Store module: errorStore module use to handle error message dispaly in snackbar
 *
 * err: Error message content as JSON Object: "err" variable is listened by watcher. Value change
 * triggers the display of message in snackbar (refer error-snackbar component)
 */
export const state = () => ({
  err: {
    code: { type: Number, default: null },
    msg: { type: String, default: null },
  },
})

/**
 * mutations are used to change state value from errorStore
 */
export const mutations = {
  /**
   * setError(): Mutator method to set "err" value to state
   *
   * @param {state} state of this store module
   * @param {JSON object} data that contain error information
   */
  setError(state, data) {
    state.err = data
  },
}

/**
 * err(): Getter for state value "err" level nomenclature items.
 *
 * @param {state} state of this store module
 * @return {JSON object} returns the "err" object
 */
export const getters = {
  err(state) {
    return state.err
  },
}
