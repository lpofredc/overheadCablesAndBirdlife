<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="poleData"
      :items-per-page="5"
      class="elevation-1"
    ></v-data-table>
  </div>
</template>

<script>
// import { FeatureCollection } from 'geojson'
export default {
  name: 'PointDisplay',
  // props: { poleData: FeatureCollection },

  data() {
    return {
      headers: [
        {
          text: 'ID Poles',
          align: 'start',
          sortable: true,
          value: 'properties.id',
        },
        { text: 'Entité', value: 'properties.owner.label' },
      ],
    }
  },
  // async fetch() {
  //   console.log('JE FETCH !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
  //   const data = (this.infrst = await this.$axios.$get(
  //     'cables/infrastructures/'
  //   ))
  //   this.$store.commit('mydata', data)
  // },
}
</script>
