<template>
  <div>
    <v-radio-group v-model="display" row dense @change="source">
      <v-row justify="space-around">
        <v-radio :label="$t('display.all')" value="both"></v-radio>
        <v-radio :label="$t('support.supports')" value="poles"></v-radio>
        <v-radio :label="$t('display.lines')" value="segments"></v-radio></v-row> </v-radio-group><v-data-table
      :headers="tableHeaders" :items="selectedData" :items-per-page="5" class="elevation-1" @click:row="showDetail">
      <template v-slot:item.properties.actions_infrastructure.0.neutralized="{ item }">
        <v-icon :color="[item.properties.actions_infrastructure[0].neutralized] == 'true'
            ? 'green'
            : 'red'
          " dark>{{
    item.properties.actions_infrastructure[0].neutralized
    ? 'mdi-check-circle'
    : 'mdi-checkbox-blank-circle'
  }}</v-icon>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'InfrastructureDisplay',

  data() {
    return {
      singleExpand: false,
      expanded: [],
      display: 'both',
      selectedData: [],
      tableHeaders: [
        {
          text: this.$t('app.id'),
          align: 'start',
          sortable: true,
          value: 'properties.id',
        },
        { text: this.$t('app.type'), value: 'resourcetype' },
        { text: this.$t('support.owner'), value: 'properties.owner.label' },
        { text: 'Notation', value: 'score' },
        {
          text: 'Neutralisé',
          value: 'properties.actions_infrastructure.0.neutralized',
        },
        {
          text: 'Dernier diagnostic',
          value: 'properties.actions_infrastructure.0.date',
        },
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
    showDetail(evt) {
      if (evt.resourcetype === 'Point') {
        this.$router.push(`/supports/${evt.properties.id}`)
      } else if (evt.resourcetype === 'Line') {
        this.$router.push(`/lines/${evt.properties.id}`)
      }
    },
  },
}
</script>
