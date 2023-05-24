<template>
  <div>
    <v-radio-group v-model="display" row density="compact">
      <v-row justify="space-around">
        <v-col><v-radio :label="$t('display.all')" value="both" /></v-col>
        <v-col><v-radio :label="$t('support.supports')" value="poles" /></v-col>
        <v-col><v-radio :label="$t('display.lines')" value="segments" /></v-col>
      </v-row>
    </v-radio-group>

    <v-data-table :headers="tableHeaders" :items="dataSource[display]" :items-per-page="5" class="elevation-1"
      @click:row="showDetail">
      <template #item.properties.actions_infrastructure.0.neutralized="{ item }">
        <v-icon :color="[item.properties.actions_infrastructure[0].neutralized] == 'true'
          ? 'green'
          : 'red'
          " dark>
          {{
            item.properties.actions_infrastructure[0].neutralized
            ? 'mdi-check-circle'
            : 'mdi-checkbox-blank-circle'
          }}
        </v-icon>
      </template>
    </v-data-table>
    {{ selectedData }}
  </div>
</template>

<script setup>
// import { mapState } from 'pinia'
import { VDataTable } from 'vuetify/labs/VDataTable'
import { useCablesStore } from '~/store/cablesStore'

const router = useRoute()

// const singleExpand = ref(false)
// const expanded = reactive([])
const display = ref('both')
const selectedData = reactive([])
const tableHeaders = reactive([
  {
    // text: $t('app.id'),
    text: 'id',
    align: 'start',
    sortable: true,
    value: 'properties.id'
  },
  // { text: $t('app.type'), value: 'resourcetype' },
  { text: 'type', value: 'resourcetype' },
  // { text: $t('support.owner'), value: 'properties.owner.label' },
  { text: 'Owner', value: 'properties.owner.label' },
  { text: 'Notation', value: 'score' },
  {
    text: 'Neutralisé',
    value: 'properties.actions_infrastructure.0.neutralized'
  },
  {
    text: 'Dernier diagnostic',
    value: 'properties.actions_infrastructure.0.date'
  }
])

const cableStore = useCablesStore()
const dataSource = reactive({
  both: cableStore.getInfstrDatafeatures,
  poles: cableStore.getPointDataFeatures,
  segments: cableStore.getLineDataFeatures
})

const setInfrstrData = async (filter) => {
  const data = await useFetch('/api/v1/cables/infrastructures', filter)
  console.log('DATA', data)
  cableStore.setInfrstrData(data)
}

onMounted(() => {
  setInfrstrData({})
})

// const source = (choice) => {
//   switch (choice) {
//     case 'both':
//       selectedData = infstrDataFeatures
//       break
//     case 'poles':
//       selectedData = pointDataFeatures
//       break
//     case 'segments':
//       selectedData = lineDataFeatures
//       break
//     default:
//     // TODO raise an exception and handle it or display message to user
//   }
// }
const showDetail = (evt) => {
  if (evt.resourcetype === 'Point') {
    router.push(`/supports/${evt.properties.id}`)
  } else if (evt.resourcetype === 'Line') {
    router.push(`/lines/${evt.properties.id}`)
  }
}

// export default {
//   name: 'InfrastructureDisplay',

//   data() {
//     return {
//       singleExpand: false,
//       expanded: [],
//       display: 'both',
//       selectedData: [],
//       tableHeaders: [
//         {
//           text: this.$t('app.id'),
//           align: 'start',
//           sortable: true,
//           value: 'properties.id',
//         },
//         { text: this.$t('app.type'), value: 'resourcetype' },
//         { text: this.$t('support.owner'), value: 'properties.owner.label' },
//         { text: 'Notation', value: 'score' },
//         {
//           text: 'Neutralisé',
//           value: 'properties.actions_infrastructure.0.neutralized',
//         },
//         {
//           text: 'Dernier diagnostic',
//           value: 'properties.actions_infrastructure.0.date',
//         },
//       ],
//     }
//   },
//   async fetch() {
//     const data = await useFetch('/api/v1/cables/infrastructures') // get FeatureCollection
//     this.$store.commit('cablesStore/add', data)
//     // needed to load data at start
//     this.selectedData = this.infstrDataFeatures
//   },
//   computed: {
//     ...mapState(useCablesStore, ['infstrDataFeatures', 'pointDataFeatures', 'lineDataFeatures'])
//   },
//   methods: {
//     source(choice) {
//       switch (choice) {
//         case 'both':
//           this.selectedData = this.infstrDataFeatures
//           break
//         case 'poles':
//           this.selectedData = this.pointDataFeatures
//           break
//         case 'segments':
//           this.selectedData = this.lineDataFeatures
//           break
//         default:
//         // TODO raise an exception and handle it or display message to user
//       }
//     },
//     showDetail(evt) {
//       if (evt.resourcetype === 'Point') {
//         this.$router.push(`/supports/${evt.properties.id}`)
//       } else if (evt.resourcetype === 'Line') {
//         this.$router.push(`/lines/${evt.properties.id}`)
//       }
//     },
//   },
// }
</script>
