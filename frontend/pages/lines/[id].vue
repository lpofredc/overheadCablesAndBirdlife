<template>
  <v-container fill-height fluid class="pa-0">
    <v-row v-if="lgAndUp" class="fill-height">
      <v-col cols="6" class="pr-0 pt-0 pb-0">
        <map-component :edit-mode="false" />
      </v-col>
      <v-col cols="6" class="pa-0">
        <data-line-detail :data="data" />
      </v-col>
    </v-row>

    <v-tabs v-if="mdAndDown" fixed-tabs class="fill-height" bg-color="indigo">
      <v-tab> {{ $t('app.map') }} </v-tab>
      <v-tab-item>
        <map-component :edit-mode="false" />
      </v-tab-item>
      <v-tab> {{ $t('app.data') }} </v-tab>
      <v-tab-item>
        <data-line-detail :data="data" />
      </v-tab-item>
    </v-tabs>
  </v-container>
</template>

<script setup>
import { useDisplay } from 'vuetify'

const route = useRoute()
const { lgAndUp, mdAndDown } = useDisplay()
const { data: data } = await useFetch(`/api/v1/cables/infrastructures/${route.params.id}`)
</script>
