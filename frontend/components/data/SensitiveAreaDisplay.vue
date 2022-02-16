<template>
  <v-data-table
    :headers="headers"
    :items="saData"
    :items-per-page="5"
    class="elevation-1"
  ></v-data-table>
</template>

<script>
import { FeatureCollection } from 'geojson'
export default {
  name: 'SensitiveAreaDisplay',
  props: { saData: FeatureCollection },

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
}
</script>
