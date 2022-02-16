
  <!--<template>
  <v-data-table
    :headers="headers"
    :items="mortalityData"
    :items-per-page="5"
    class="elevation-1"
  ></v-data-table>
</template>

<script>
import { FeatureCollection } from 'geojson'
export default {
  name: 'MortalityDisplay',
  props: { mortalityData: FeatureCollection },

  data() {
    return {
      headers: [
        {
          text: 'ID Mortalité',
          align: 'start',
          sortable: true,
          value: 'properties.id',
        },
        // { text: 'Entité', value: 'properties.owner.label' },
      ],
    }
  },
}
</script>
