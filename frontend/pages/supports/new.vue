<template>
  <NuxtLayout name="view">
    <template #map><map-search :edit-mode="true" mode="point" /></template>
    <form-point />
  </NuxtLayout>
</template>
