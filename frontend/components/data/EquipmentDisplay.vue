
<template>
  <div>
    coucou
    <v-radio-group v-model="display" row dense @change="source">
      <v-row justify="space-around">
        <v-radio :label="$t('display.all')" value="both"></v-radio>
        <v-radio :label="$t('display.eqmt_poles ')" value="poles"></v-radio>
        <v-radio
          :label="$t('display.eqmt_segments')"
          value="segments"
        ></v-radio></v-row
    ></v-radio-group>
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
  name: 'EquipmentDisplay',

  data() {
    return {
      display: 'both',
      selectedData: [],
      headers: [
        {
          text: this.$t('app.id'),
          align: 'start',
          sortable: true,
          value: 'id',
        },
        // { text: 'TMP', value: 'eqmt_type.label' },
      ],
    }
  },
  async fetch() {
    const pointOpData = await this.$axios.$get('cables/operations/?type=14')
    const lineOpData = await this.$axios.$get('cables/operations/?type=13')
    const opData = await this.$axios.$get('cables/operations')
    this.$store.commit('cablesStore/addOperation', {
      all: opData,
      point: pointOpData,
      line: lineOpData,
    })
    // needed to load data at start
    this.selectedData = this.opData
  },
  computed: mapGetters({
    opData: 'cablesStore/opData',
    pointOpData: 'cablesStore/pointOpData',
    LineOpData: 'cablesStore/LineOpData',
  }),
  methods: {
    source(choice) {
      switch (choice) {
        case 'both':
          this.selectedData = this.opData
          break
        case 'poles':
          this.selectedData = this.pointOpData
          break
        case 'segments':
          this.selectedData = this.lineOpData
          break
        default:
        // TODO raise an exception and handle it or display message to user
      }
    },
  },
}
</script>
