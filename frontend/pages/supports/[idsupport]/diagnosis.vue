<template>
  <v-container class="fill-height pa-0">
    <v-row v-if="mdAndUp" class="fill-height">
      <v-col class="pr-0 pt-0 pb-0">
        <map-search :edit-mode="true" mode="point" />
      </v-col>
      <v-col class="pa-0">
        <form-point :diagnosis="diag" />
      </v-col>
    </v-row>

    <template v-if="!mdAndUp">
      <v-tabs v-model="tab" align-tabs="title" fixed-tabs>
        <v-tab> {{ $t('app.map') }} </v-tab>
        <v-tab> {{ $t('app.data') }} </v-tab>
      </v-tabs>

      <v-tabs-items v-model="tab" class="fill-height">
        <v-tab-item>
          <map-search :edit-mode="true" mode="point" />
        </v-tab-item>
        <v-tab-item>
          <form-point :diagnosis="data" />
        </v-tab-item>
      </v-tabs-items>
    </template>
  </v-container>
</template>


<script setup>
import { useDisplay } from 'vuetify'
const { mdAndUp } = useDisplay()
definePageMeta({
  auth: true,
});
const route = useRoute()
const diag = route.query.id_diagnosis ? await useHttp(`/api/v1/cables/diagnosis/${route.query.id_diagnosis}`) : null
</script>
