<template>
  <NuxtLayout name="view">
    <template #map>
      <map :edit-mode="false" />
    </template>
    <data-line-detail :data="data" />
  </NuxtLayout>
</template>


<script setup>
definePageMeta({
  auth: true,
});
const route = useRoute()
const { data: data } = await useHttp(`/api/v1/cables/infrastructures/${route.params.id}`)
</script>
