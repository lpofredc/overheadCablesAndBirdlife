<template>
  <NuxtLayout name="view">
    <template #map>
      <map :edit-mode="false" />
    </template>
    <data-operation-detail :data="data" />
  </NuxtLayout>
</template>


<script setup>
definePageMeta({
  auth: true,
});
const route = useRoute()
const { data: data } = await useHttp(`cables/operations/${route.params.id}`)
</script>
