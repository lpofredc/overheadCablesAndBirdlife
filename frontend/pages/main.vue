
<template>
  <div>
    <v-row v-if="$vuetify.breakpoint.lgAndUp"
      ><v-col><data-map :my-data="mydata" /></v-col
      ><v-col><data-display :my-data="mydata" /></v-col
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
      <v-tab-item> <data-display :my-data="mydata" /> </v-tab-item>
    </v-tabs>
  </div>
</template>

<script>
export default {
  name: 'MainPage',
  auth: false,
  data() {
    return {
      app_name: 'Overhead Cables & BirdLife',
      drawer_opened: true, // drawer closed by default
      miniVariant: true, // wide drawer when opening by default
      mydata: [],
    }
  },
  async fetch() {
    this.mydata = await this.$axios.$get('cables/infrastructures  ')
  },
  methods: {
    openDrawer() {
      return this.$auth.loggedIn ? this.drawer_opened : false
    },
  },
}
</script>
