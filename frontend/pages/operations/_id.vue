<template>
  <div>
    <v-row v-if="$vuetify.breakpoint.lgAndUp"
      ><v-col width="50%"> <map-component /> </v-col><v-col></v-col
    ></v-row>
    <v-tabs
      v-if="$vuetify.breakpoint.mdAndDown"
      fixed-tabs
      background-color="indigo"
      dark
    >
      <v-tab> {{ $t('app.map') }} </v-tab>
      <v-tab-item>
        <map-component />
      </v-tab-item>
      <v-tab> {{ $t('app.data') }} </v-tab>
      <v-tab-item> </v-tab-item>
    </v-tabs>
  </div>
</template>

<script>
export default {
  name: 'OperationDetailPage',
  async asyncData({ $axios, params }) {
    return {
      data: await $axios.$get(`cables/operations/${params.id}`),
    }
  },
  data() {
    return {
      drawer_opened: true, // drawer closed by default
      miniVariant: true, // wide drawer when opening by default
    }
  },
}
</script>
