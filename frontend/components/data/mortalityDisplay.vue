<template>
  <v-data-table v-model:items-per-page="itemsPerPage" :headers="headers" :items="mortalityStore.getMortalityFeatures"
    item-value="name" class="elevation-1" density="compact"></v-data-table>
</template>

<script setup lang="ts">
// import { FeatureCollection } from 'geojson'
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

onMounted(() => {
  // setInfrstrData({})
  console.log('mortalityStore', mortalityStore)
  mortalityStore.getMortalityData()
})
mortalityData.value
</script>
