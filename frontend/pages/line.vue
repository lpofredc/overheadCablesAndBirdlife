<template>
  <div>
    <v-row v-if="$vuetify.breakpoint.lgAndUp"
      ><v-col width="50%"><map-component :edit-mode="true" mode="line" /></v-col
      ><v-col><form-line-component /></v-col
    ></v-row>
    <v-tabs
      v-if="$vuetify.breakpoint.mdAndDown"
      fixed-tabs
      background-color="indigo"
      dark
    >
      <v-tab> {{ $t('app.map') }} </v-tab>
      <v-tab-item> <map-component :edit-mode="true" mode="line" /> </v-tab-item>
      <v-tab> {{ $t('app.data') }} </v-tab>
      <v-tab-item> <form-line-component /> </v-tab-item>
    </v-tabs>
  </div>
</template>

<script>
export default {
  name: 'LinePage',
  data() {
    return {
      drawer_opened: true, // drawer closed by default
      miniVariant: true, // wide drawer when opening by default
    }
  },
}
</script>
