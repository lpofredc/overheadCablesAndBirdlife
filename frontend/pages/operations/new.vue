<template>
  <NuxtLayout name="view">
    <template #map>
      <map :edit-mode="true" mode="point" />
    </template>
    <form-point />
  </NuxtLayout>
</template>


<script setup>
definePageMeta({
  auth: true,
});
</script>
