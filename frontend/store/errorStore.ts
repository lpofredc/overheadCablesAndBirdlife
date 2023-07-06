/** Nuxt Store module: errorStore module use to handle error message dispaly in snackbar
 *
 * err: Error message content as JSON Object: "err" variable is listened by watcher. Value change
 * triggers the display of message in snackbar (refer error-snackbar component)
 */

import { defineStore } from "pinia";

export interface ErrorInfo {
  code: number | null;
  msg: string | null;
}

export const useErrorsStore = defineStore("errors", {
  state: () => ({
    err: {} as ErrorInfo,
  }),
  getters: {
    /**
     * err(): Getter for state value "err" level nomenclature items.
     *
     * @param {state} state of this store module
     * @return {JSON object} returns the "err" object
     */
    getError(state) {
      return state.err;
    },
  },
  actions: {
    setError(err: ErrorInfo) {
      this.err = err;
    },
  },
});
