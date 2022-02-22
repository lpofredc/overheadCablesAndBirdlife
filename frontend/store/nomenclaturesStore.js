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
   * Getter for Sensitive Area data as geoJson object
   *
   * @param {state} context of this store module
   * @return {geoJson object} contains Sensitive Area data
   */
  nomenclatures(state) {
    return state.nomenclatures
  },
}

export const actions = {
  /**
   * Store method to gather nomenclatures data in store (nomenclaturesStore)
   * Create a dictionnary with all Types, and each Type contains an array of Items.
   *
   * @param {context} context object set as destructured form { commit }
   */
  async getNomenclatures({ commit }) {
    try {
      const types = await this.$axios.$get('nomenclature/types') // get Types list

      // For each type, get list of items
      for (const i in types) {
        let items = await this.$axios.$get(
          `nomenclature/type/${types[i].id}/items`
        )
        // Filter to keep only Items matching to current Type (request send the whole list)
        items = items.filter((elem) => elem.type === types[i].id)

        // TODO review sinp_nomanclature in backend => nomenclature/type/${types[i].id}/items` send
        // the list of all items, whatever the "${types[i].id}" is
        types[i].items = items
      }
      commit('add', types)
    } catch (e) {
      $nuxt.error({
        statusCode: 512,
        message:
          "Un problème est survenu pour le chargement des données de paramétrage de l'application",
      })
    }
  },
}
