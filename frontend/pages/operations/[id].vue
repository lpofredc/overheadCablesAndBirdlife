<template>
  <div>
    <v-row v-if="lgAndUp">
      <v-col width="50%">
        <map-component />
      </v-col><v-col>
        <data-operation-detail :data="data" />
      </v-col>
    </v-row>
    <v-tabs v-if="mdAndDown" fixed-tabs bg-color="indigo">
      <v-tab> {{ $t('app.map') }} </v-tab>
      <v-tab-item>
        <map-component />
      </v-tab-item>
      <v-tab> {{ $t('app.data') }} </v-tab>
      <v-tab-item>
        <data-operation-detail :data="data" />
      </v-tab-item>
    </v-tabs>
  </div>
</template>

<script setup>
import { useDisplay } from 'vuetify'
const { lgAndUp, mdAndDown } = useDisplay()

const route = useRoute()
const { data: data } = await useFetch(`cables/operations/${route.params.id}`)
</script>
