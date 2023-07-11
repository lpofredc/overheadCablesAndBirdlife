<template>
  <NuxtLayout name="view">
    <template #map><map-search :edit-mode="true" mode="point" /></template>
    <form-point :diagnosis="diag" />
  </NuxtLayout>
</template>



<script setup>
definePageMeta({
  auth: true,
});
const route = useRoute()
const diag = route.query.id_diagnosis ? await useHttp(`/api/v1/cables/diagnosis/${route.query.id_diagnosis}`) : null
</script>
