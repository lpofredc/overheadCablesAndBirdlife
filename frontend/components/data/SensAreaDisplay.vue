<template>
  <v-data-table
    :headers="headers"
    :items="SADataFeatures"
    :items-per-page="5"
    class="elevation-1"
  ></v-data-table>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'SensAreaDisplay',
  data() {
    return {
      headers: [
        {
          text: 'ID Zone Sensible',
          align: 'start',
          sortable: true,
          value: 'id',
        },
        { text: 'Name', value: 'properties.name' },
        { text: 'Code', value: 'properties.code' },
      ],
    }
  },
  async fetch() {
    const data = await this.$axios.$get('sensitive-areas/') // get FeatureCollection
    this.$store.commit('SAStore/add', data)
  },
  computed: mapGetters({ SADataFeatures: 'SAStore/SADataFeatures' }),
}
</script>
