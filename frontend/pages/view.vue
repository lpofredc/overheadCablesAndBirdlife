<template>
  <v-container fill-height fluid class="pa-0">
    <v-row v-if="$vuetify.breakpoint.lgAndUp" class="fill-height">
      <v-col cols="6" class="pr-0 pt-0 pb-0">
        <map-component :edit-mode="false" />
      </v-col>
      <v-col cols="6" class="pa-0">
        <display-component />
      </v-col>
    </v-row>

    <v-tabs
      v-if="$vuetify.breakpoint.mdAndDown"
      fixed-tabs
      class="fill-height"
      background-color="indigo"
      dark
    >
      <v-tab> {{ $t('app.map') }} </v-tab>
      <v-tab-item>
        <map-component :edit-mode="false" />
      </v-tab-item>
      <v-tab> {{ $t('app.data') }} </v-tab>
      <v-tab-item>
        <display-component />
      </v-tab-item>
    </v-tabs>
  </v-container>
</template>

<script>
export default {
  name: 'ViewComponent',
  data() {
    return {
      drawer_opened: true, // drawer closed by default
      miniVariant: true, // wide drawer when opening by default
    }
  },
  mounted() {
    // Loading of Nomenclatures needed to get data to set up the application
    // Implemented there as authentification needed
    this.$store.dispatch('nomenclaturesStore/loadNomenclatures')
    // initialize coordinatesStore with newPointCoord at null
    this.$store.commit('coordinatesStore/addPointCoord', {
      lat: null,
      lng: null,
    })
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
