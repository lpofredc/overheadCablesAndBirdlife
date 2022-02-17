
<template>
  <div>
    <v-row v-if="$vuetify.breakpoint.lgAndUp"
      ><v-col width="50%"><data-map :cables-data="infrst" /></v-col
      ><v-col
        ><data-display
          :sa-data="SAreas"
          :mortality-data="mortality"
          :pole-data="poles"
          :segment-data="segments" /></v-col
    ></v-row>

    <v-tabs
      v-if="$vuetify.breakpoint.mdAndDown"
      fixed-tabs
      background-color="indigo"
      dark
    >
      <v-tab> Map </v-tab>
      <v-tab-item> <data-map :cables-data="infrst" /> </v-tab-item>
      <v-tab> DataDisplay </v-tab>
      <v-tab-item>
        <data-display
          :sa-data="SAreas"
          :mortality-data="mortality"
          :pole-data="poles"
          :segment-data="segments"
        />
      </v-tab-item>
    </v-tabs>
  </div>
</template>

<script>
export default {
  name: 'MainPage',
  // auth: false,
  data() {
    return {
      app_name: 'Overhead Cables & BirdLife',
      drawer_opened: true, // drawer closed by default
      miniVariant: true, // wide drawer when opening by default
      infrst: [], // geojson data for infrastructures (poles and segments)
      poles: [], // geojson data for poles
      segments: [], // geojson data for poles
      SAreas: [], // geojson data for sensitive areas
      mortality: [], // geojson data for mortality cases
    }
  },
  async fetch() {
    this.infrst = await this.$axios.$get('cables/infrastructures/')
    this.poles = this.infrst.filter((item) => item.resourcetype === 'Pole')
    this.segments = this.infrst.filter(
      (item) => item.resourcetype === 'Segment'
    )
    this.SAreas = await this.$axios.$get('sensitive-areas/')
    this.SAreas = this.SAreas.features
    this.mortality = await this.$axios.$get('mortality/')
  },
  methods: {
    openDrawer() {
      return this.$auth.loggedIn ? this.drawer_opened : false
    },
  },
}
</script>
