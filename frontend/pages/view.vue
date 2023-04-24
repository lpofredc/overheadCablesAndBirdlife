<template>
  <v-container fill-height fluid class="pa-0">
    <v-row v-if="$vuetify.breakpoint.mdAndUp" class="fill-height">
      <v-col cols="6" class="pr-0 pt-0 pb-0">
        <map-component :edit-mode="false" />
      </v-col>
      <v-col cols="6" class="pa-0">
        <display-component />
      </v-col>
    </v-row>

    <template v-if="!$vuetify.breakpoint.mdAndUp">
      <v-tabs v-model="tab" align-with-title fixed-tabs>
        <v-tab> {{ $t('app.map') }} </v-tab>
        <v-tab> {{ $t('app.data') }} </v-tab>
      </v-tabs>

      <v-tabs-items v-model="tab" class="fill-height">
        <v-tab-item>
          <map-component :edit-mode="false" />
        </v-tab-item>
        <v-tab-item>
          <display-component />
        </v-tab-item>
      </v-tabs-items>
    </template>
  </v-container>
</template>

<script>
export default {
  name: 'ViewComponent',
  data() {
    return {
      tab: null,
    }
  },
  mounted() {
    /**
     * Call of "loadNomenclatures" action from nomenclaturesStore to load Nomenclatures needed to
     * get data to set up the application.
     * Implemented here as authentification needed
     */
    this.$store.dispatch('nomenclaturesStore/loadNomenclatures')
    /**
     * Call of "addPointCoord" action from coordinatesStore to linitialize newPointCoord at null
     */
    this.$store.commit('coordinatesStore/addPointCoord', {
      lat: null,
      lng: null,
    })
  },
}
</script>
