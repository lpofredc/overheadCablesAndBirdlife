<template>
  <v-container class="fill-height pa-0">
    <v-row v-if="mdAndUp" class="fill-height">
      <v-col cols="6" class="pr-0 pt-0 pb-0">
        <map-component :edit-mode="true" mode="point" />
      </v-col>
      <v-col cols="6" class="pa-0">
        <form-point-component />
      </v-col>
    </v-row>

    <template v-if="!mdAndUp">
      <v-card class="fill-height" width="100%">
        <v-tabs v-model="tab" align-tabs="title" fixed-tabs>
          <v-tab value="map"> {{ $t('app.map') }} </v-tab>
          <v-tab value="data"> {{ $t('app.data') }} </v-tab>
        </v-tabs>

        <v-card-text class="fill-height pa-0">
          <v-window v-model="tab" class="fill-height">
            <v-window-item value="map" class="fill-height">
              <map-component :edit-mode="true" mode="point" />
            </v-window-item>
            <v-window-item value="data">
              <form-point-component />
            </v-window-item>
          </v-window>
        </v-card-text>
      </v-card>
    </template>
  </v-container>
</template>

<script setup>
import { useDisplay } from 'vuetify'

const { mdAndUp } = useDisplay()
const tab=ref(null)
</script>
