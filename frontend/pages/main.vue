<template>
  <div>
    <v-row v-if="$vuetify.breakpoint.lgAndUp"
      ><v-col width="50%"><data-map /></v-col><v-col><data-display /></v-col
    ></v-row>

    <v-tabs
      v-if="$vuetify.breakpoint.mdAndDown"
      fixed-tabs
      background-color="indigo"
      dark
    >
      <v-tab> Map </v-tab>
      <v-tab-item> <data-map /> </v-tab-item>
      <v-tab> DataDisplay </v-tab>
      <v-tab-item>
        <data-display />
      </v-tab-item>
    </v-tabs>
  </div>
</template>

<script>
export default {
  name: 'MainPage',
  data() {
    return {
      app_name: 'Overhead Cables & BirdLife',
      drawer_opened: true, // drawer closed by default
      miniVariant: true, // wide drawer when opening by default
    }
  },
  /**
   * Fetch method to gather nomenclatures data in store (nomenclaturesStore)
   * Implemented there as authentification needed.
   * Create a dictionnary with all Types, and each Type contains an array of Items
   */
  async fetch() {
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
    this.$store.commit('nomenclaturesStore/add', types)
  },
  /**
   * Manage opening/closing drawer menu
   */
  methods: {
    openDrawer() {
      return this.$auth.loggedIn ? this.drawer_opened : false
    },
  },
}
</script>
