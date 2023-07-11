<template>
  <NuxtLayout name="view">
    <template #map><map-search :edit-mode="false" /></template>
    <display-component />
  </NuxtLayout>
</template>

<script setup>
import {ref} from 'vue'
import {useDisplay} from 'vuetify'

definePageMeta({
  auth: true
})

const tab = ref(null)
const {mdAndUp} = useDisplay()

onMounted (() => {
  console.log(`the component is now mounted. mdAndUp`, mdAndUp.value)
})

</script>
