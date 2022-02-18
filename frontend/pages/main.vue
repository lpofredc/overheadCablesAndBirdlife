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
  methods: {
    openDrawer() {
      return this.$auth.loggedIn ? this.drawer_opened : false
    },
  },
}
</script>
