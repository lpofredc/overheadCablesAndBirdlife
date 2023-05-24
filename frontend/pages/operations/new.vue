<template>
  <div style="height: 90vh" class="overflow-auto">
    <v-row v-if="lgAndUp">
      <v-col width="50%">
        <map-component :edit-mode="true" mode="point" />
      </v-col><v-col><form-point-component /></v-col>
    </v-row>
    <v-tabs v-if="mdAndDown" fixed-tabs bg-color="indigo">
      <v-tab> {{ $t('app.map') }} </v-tab>
      <v-tab-item>
        <map-component :edit-mode="true" mode="point" />
      </v-tab-item>
      <v-tab> {{ $t('app.data') }} </v-tab>
      <v-tab-item> <form-point-component /> </v-tab-item>
    </v-tabs>
  </div>
</template>

<script setup>
import { useDisplay } from 'vuetify'
const { lgAndUp, mdAndDown } = useDisplay()
</script>
