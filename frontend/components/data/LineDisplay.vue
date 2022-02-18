<template>
  <v-data-table
    :headers="headers"
    :items="segmentData"
    :items-per-page="5"
    class="elevation-1"
  ></v-data-table>
</template>

<script>
import { FeatureCollection } from 'geojson'
export default {
  name: 'LineDisplay',
  props: { segmentData: FeatureCollection },

  data() {
    return {
      headers: [
        {
          text: 'ID Segments',
          align: 'start',
          sortable: true,
          value: 'properties.id',
        },
        { text: 'Entité', value: 'properties.owner.label' },
      ],
    }
  },
}
</script>
