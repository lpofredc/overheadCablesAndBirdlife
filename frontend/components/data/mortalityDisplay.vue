<template>
  <v-data-table v-model:items-per-page="itemsPerPage" :headers="headers" :items="mortalityStore.getMortalityFeatures"
    item-value="name" class="elevation-1" density="compact" @click:row="rowClickEvent">
    <template v-slot:item.id="{ item }">
      <v-chip link :to="`/mortality/${item.raw.id}`">
        {{item.raw.id}}
      </v-chip>
    </template>
  </v-data-table>
</template>

<script setup lang="ts">
import { useCoordinatesStore } from '../../store/coordinatesStore'

// import { FeatureCollection } from 'geojson'
const router =useRouter()
const itemsPerPage=ref(5)
const mortalityData = ref([])
const headers = reactive([
  {title: 'ID', align: 'start',sortable:true, key: 'id'},
  {title: 'Nom vernaculaire', align: 'start',sortable:true, key: 'properties.species.vernacular_name'},
  {title: 'Nom scientifique', align: 'start',sortable:true, key: 'properties.species.scientific_name'},
  {title: 'Date', align: 'center',sortable:true, key: 'properties.date'},
  {title: 'Cause', align: 'center',sortable:true, key: 'properties.death_cause.label'},
])

const mortalityStore = useMortalityStore()
const coordinatesStore = useCoordinatesStore()

const showDetail = (_, {item}) => {
  const rowData = item.columns
  router.push(`/mortality/${rowData['id']}`)
}

const zoomTo = (item) => {
  coordinatesStore.setCenter([...item.geometry.coordinates].reverse())
  coordinatesStore.setZoom(14)
}
const routerPushUrl =  (item) => {
  console.log('routerPushUrl', item.resourcetype)
    if (item.resourcetype === 'Point') {
    return `/mortality/${item.properties.id}`
  } else if (item.resourcetype === 'Line') {
    return `/lines/${item.properties.id}`
  }
}

const rowClickEvent = (_, {item}) => {
  zoomTo(item.raw)
  // console.log('rowClickEvent', item.raw.resourcetype)
  // if (item.raw.resourcetype === 'Point') {
  //   router.push(`/supports/${item.raw.properties.id}`)
  // } else if (item.raw.resourcetype === 'Line') {
  //   router.push(`/lines/${item.raw.properties.id}`)
  // }
}

onMounted(() => {
  // setInfrstrData({})
  mortalityStore.getMortalityData()
})
</script>
