/** Nuxt Store module: errorStore module use to handle error message dispaly in snackbar
 *
 * err: Error message content as JSON Object: "err" variable is listened by watcher. Value change
 * triggers the display of message in snackbar (refer error-snackbar component)
 */

import { defineStore, acceptHMRUpdate } from 'pinia'

export const useErrorsStore = defineStore('errors', {
  state: () => ({
    err: {
      code: { type: Number, default: null },
      msg: { type: String, default: null }
    }
  }),
  getters: {
    /**
     * err(): Getter for state value "err" level nomenclature items.
     *
     * @param {state} state of this store module
     * @return {JSON object} returns the "err" object
     */
    err (state) {
      return state.err
    }
  }
})

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useErrorsStore, import.meta.hot))
}
