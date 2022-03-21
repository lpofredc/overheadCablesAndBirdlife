<!-- <template>
  <v-container fill-height fluid class="pa-0">
    <v-row v-if="$vuetify.breakpoint.lgAndUp" class="fill-height">
      <v-col cols="6" class="pr-0 pt-0 pb-0">
        <map-component :edit-mode="true" mode="point" />
      </v-col>
      <v-col cols="6" class="pa-0" style="background-color: red">
        <form-point-update-component />
      </v-col>
    </v-row>
    <v-tabs
      v-if="$vuetify.breakpoint.mdAndDown"
      fixed-tabs
      background-color="indigo"
      dark
    >
      <v-tab> {{ $t('app.map') }} </v-tab>
      <v-tab-item>
        <map-component :edit-mode="true" mode="point" />
      </v-tab-item>
      <v-tab> {{ $t('app.data') }} </v-tab>
      <v-tab-item>
        <form-point-update-component />
      </v-tab-item>
    </v-tabs>
  </v-container>
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
//   this.$store.dispatch('nomenclaturesStore/loadNomenclatures')
// },
// /**
//  * Manage opening/closing drawer menu
//  */
// methods: {
//   openDrawer() {
//     return this.$auth.loggedIn ? this.drawer_opened : false
//   },
// },
</script> -->
