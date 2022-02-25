/** Nuxt Store module: NomenclatureStore for Nomenclature module
 *
 * Nomenclature define Source, Type and Item data. It works as a data dictionnary for the
 * application. Each Type is associated to a Source and each Item is associated to a Type.
 * Lot of fields in the DataBase Model from backend are associated to a Type. Thet means that
 * acceptable values for these fieds are all Items related to this field.
 * This allow standardisation and securisation of data recorded in DB, and in same time assuring
 * flexibility as the application remain configurable by updation Source/Type/Item in DB. *
 */
export const state = () => ({
  /** Sensible Area data get from fetch request as geoJson object */
  nomenclatures: {},
})

export const mutations = {
  /**
   * Mutation: apply value change to state of current store module
   *
   * @param {state} state of this store module
   * @param {geoJson object} contains Sensitive Area data get from fetch request
   */
  add(state, data) {
    state.nomenclatures = data
  },
}

export const getters = {
  /**
   * Getter for infrastructure condition nomenclature items.
   *
   * @param {state} state of this store module
   * @return {JSON object} returns the list of nomenclature items for infrastucture conditions
   */
  getConditions(state) {
    try {
      const cond = state.nomenclatures.find(
        (elem) => elem.mnemonic === 'infrastr_condition'
      )
      return cond.items
    } catch (_err) {
      $nuxt.error({
        statusCode: errorCodes.get_infrstr_conditions.code,
        message:
          `Error ${errorCodes.get_infrstr_conditions.code}: ` +
          $nuxt.$t(`error.${errorCodes.get_infrstr_conditions.msg}`),
      })
    }
  },
  /**
   * Getter for owner nomenclature items.
   *
   * @param {state} state of this store module
   * @return {JSON object} returns the list of nomenclature items for owners
   */
  getOwners(state) {
    try {
      const owners = state.nomenclatures.find(
        (elem) => elem.mnemonic === 'owner'
      )
      return owners.items
    } catch (_err) {
      $nuxt.error({
        statusCode: errorCodes.get_infrstr_owners.code,
        message:
          `Error ${errorCodes.get_infrstr_owners.code}: ` +
          $nuxt.$t(`error.${errorCodes.get_infrstr_owners.msg}`),
      })
    }
  },
  /**
   * Getter for pole type nomenclature items.
   *
   * @param {state} state of this store module
   * @return {JSON object} returns the list of nomenclature items for pole types
   */
  getPoleTypes(state) {
    try {
      const poleTypes = state.nomenclatures.find(
        (elem) => elem.mnemonic === 'pole_type'
      )
      return poleTypes.items
    } catch (_err) {
      $nuxt.error({
        statusCode: errorCodes.get_infrstr_poletypes.code,
        message:
          `Error ${errorCodes.get_infrstr_poletypes.code}: ` +
          $nuxt.$t(`error.${errorCodes.get_infrstr_poletypes.msg}`),
      })
    }
  },
  /**
   * Getter for risk level nomenclature items.
   *
   * @param {state} state of this store module
   * @return {JSON object} returns the list of nomenclature items for risk levels
   */
  getRiskLevels(state) {
    try {
      const poleTypes = state.nomenclatures.find(
        (elem) => elem.mnemonic === 'risk_level'
      )
      return poleTypes.items
    } catch (_err) {
      $nuxt.error({
        statusCode: errorCodes.get_infrstr_poletypes.code,
        message:
          `Error ${errorCodes.get_infrstr_risklevels.code}: ` +
          $nuxt.$t(`error.${errorCodes.get_infrstr_risklevels.msg}`),
      })
    }
  },
}

export const actions = {
  /**
   * Store method to gather nomenclatures data in store (nomenclaturesStore)
   * Create a dictionnary with all Types, and each Type contains an array of Items.
   *
   * @param {context} context object set as destructured form { commit }
   */
  async loadNomenclatures({ commit }) {
    try {
      const types = await this.$axios.$get('nomenclature/types') // get Types list

      // For each type, get list of items
      for (const i in types) {
        let items = await this.$axios.$get(
          `nomenclature/type/${types[i].id}/items`
        )
        // TODO To be removed
        // console.log(types[i])

        // Filter to keep only Items matching to current Type (request send the whole list)
        items = items.filter((elem) => elem.type === types[i].id)

        // TODO review sinp_nomanclature in backend => nomenclature/type/${types[i].id}/items` send
        // the list of all items, whatever the "${types[i].id}" is
        types[i].items = items
      }
      commit('add', types)
    } catch (_err) {
      $nuxt.error({
        statusCode: errorCodes.loading_whole_nomenclatures.code,
        message:
          `Error ${errorCodes.loading_whole_nomenclatures.code}: ` +
          $nuxt.$t(`error.${errorCodes.loading_whole_nomenclatures.msg}`),
      })
    }
  },
}
