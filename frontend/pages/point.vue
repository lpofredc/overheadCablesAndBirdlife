<template>
  <div>
    <v-row v-if="$vuetify.breakpoint.lgAndUp"
      ><v-col width="50%"><map-component :edit-mode="true" /></v-col
      ><v-col><form-point-component /></v-col
    ></v-row>
    <v-tabs
      v-if="$vuetify.breakpoint.mdAndDown"
      fixed-tabs
      background-color="indigo"
      dark
    >
      <v-tab> {{ $t('app.map') }} </v-tab>
      <v-tab-item> <map-component :edit-mode="true" /> </v-tab-item>
      <v-tab> {{ $t('app.data') }} </v-tab>
      <v-tab-item> <form-point-component /> </v-tab-item>
    </v-tabs>
  </div>
</template>

<script>
export default {
  name: 'PointPage',
  data() {
    return {
      drawer_opened: true, // drawer closed by default
      miniVariant: true, // wide drawer when opening by default
    }
  },
}

// },
// mounted() {
//   // Loading of Nomenclatures needed to get data to set up the application
//   // Implemented there as authentification needed.
//   this.$store.dispatch('nomenclaturesStore/getNomenclatures')
// },
// /**
//  * Manage opening/closing drawer menu
//  */
// methods: {
//   openDrawer() {
//     return this.$auth.loggedIn ? this.drawer_opened : false
//   },
// },
</script>
