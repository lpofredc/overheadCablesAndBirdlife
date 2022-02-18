<template>
  <div>
    <v-radio-group v-model="display" row dense @change="source">
      <v-row justify="space-around">
        <v-radio :label="$t('display.all')" value="both"></v-radio>
        <v-radio :label="$t('display.poles')" value="poles"></v-radio>
        <v-radio :label="$t('display.segments')" value="segments"></v-radio
      ></v-row>
    </v-radio-group>
    <v-data-table
      :headers="headers"
      :items="selectedData"
      :items-per-page="5"
      class="elevation-1"
    ></v-data-table>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'InfrastructureDisplay',

  data() {
    return {
      display: 'both',
      selectedData: [],
      headers: [
        {
          text: this.$t('app.id'),
          align: 'start',
          sortable: true,
          value: 'properties.id',
        },
        { text: this.$t('app.type'), value: 'resourcetype' },
        { text: this.$t('infra.owner'), value: 'properties.owner.label' },
      ],
    }
  },
  async fetch() {
    const data = await this.$axios.$get('cables/infrastructures') // get FeatureCollection
    this.$store.commit('cablesStore/add', data)
    // needed to load data at start
    this.selectedData = this.infstrDataFeatures
  },
  computed: mapGetters({
    infstrDataFeatures: 'cablesStore/infstrDataFeatures',
    pointDataFeatures: 'cablesStore/pointDataFeatures',
    lineDataFeatures: 'cablesStore/lineDataFeatures',
  }),
  methods: {
    source(choice) {
      switch (choice) {
        case 'both':
          this.selectedData = this.infstrDataFeatures
          break
        case 'poles':
          this.selectedData = this.pointDataFeatures
          break
        case 'segments':
          this.selectedData = this.lineDataFeatures
          break
        default:
        // TODO raise an exception and handle it or display message to user
      }
    },
  },
}
</script>
