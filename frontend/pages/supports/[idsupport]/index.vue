<template>
  <NuxtLayout name="view">
    <template #map><map-search :edit-mode="false" /></template>
    <data-support-detail :data="info.data" />
  </NuxtLayout>
</template>

<script setup>
const route = useRoute()
const { data: info } = await useAsyncData(
  'info',
  () => useHttp(`/api/v1/cables/infrastructures/${route.params.idsupport}`)
)
</script>
