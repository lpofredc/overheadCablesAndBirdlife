<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-card class="logo py-4 d-flex justify-center">
        <welcome />
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'IndexPage',
  auth: false,
  // async fetch() {
  //   const data = await this.$axios.$get('nomenclature/types') // get FeatureCollection
  //   console.log(data)
  //   this.$store.commit('nomenclaturesStore/add', data)
  //   // needed to load data at start
  //   this.selectedData = this.infstrDataFeatures
  // },
}
</script>
