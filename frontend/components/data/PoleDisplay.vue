<template>
  <v-data-table
    :headers="headers"
    :items="poleData"
    :items-per-page="5"
    class="elevation-1"
  ></v-data-table>
</template>

<script>
import { FeatureCollection } from 'geojson'
export default {
  name: 'PoleDisplay',
  props: { poleData: FeatureCollection },

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
}
</script>
