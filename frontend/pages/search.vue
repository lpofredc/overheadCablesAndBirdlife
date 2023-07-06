<template>
  <v-container tag="l2" class="fill-height pa-0" fluid>
    <v-row v-if="mdAndUp" class="fill-height">
      <v-col cols="6" class="pr-0 pt-0 pb-0">
        <map-search :edit-mode="false" />
      </v-col>
      <v-col cols="6" class="pa-0">
        <display-component />
      </v-col>
    </v-row>

    <template v-if="!mdAndUp">
      <v-card class="fill-height" width="100%">
        <v-tabs v-model="tab" align-tabs="title" fixed-tabs>
          <v-tab value="map"> {{ $t('app.map') }}</v-tab>
          <v-tab value="data"> {{ $t('app.data') }}</v-tab>
        </v-tabs>

        <v-card-text class="fill-height pa-0">
          <v-window v-model="tab" class="fill-height">
            <v-window-item value="map" class="fill-height">
              <map-search :edit-mode="false" />
            </v-window-item>
            <v-window-item value="data">
              <display-component />
            </v-window-item>
          </v-window>
        </v-card-text>
      </v-card>
    </template>
  </v-container>
</template>

<script setup>
import {ref} from 'vue'
import {useDisplay} from 'vuetify'

definePageMeta({
  auth: true
})

const tab = ref(null)
const {mdAndUp} = useDisplay()
const fluid=ref(true)

</script>
