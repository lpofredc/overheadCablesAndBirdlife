<template>
  <v-container class="fill-height pa-0">
    <v-row v-if="mdAndUp" class="fill-height">
      <v-col class="pr-0 pt-0 pb-0">
        <ClientOnly fallback-tag="span" fallback="Loading comments...">
          <map-search :edit-mode="false" />
        </ClientOnly>
      </v-col>
      <v-col class="pa-0">
        <data-support-detail :data="info.data" />
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
              <ClientOnly fallback-tag="span" fallback="Loading comments...">
                <map-search :edit-mode="false" />
              </ClientOnly>
            </v-window-item>
            <v-window-item value="data">
              <data-support-detail :data="info.data" />
            </v-window-item>
          </v-window>
        </v-card-text>
      </v-card>


      <v-tabs-items v-model="tab">
        <v-tab-item>

        </v-tab-item>
        <v-tab-item>

        </v-tab-item>
      </v-tabs-items>
    </template>
  </v-container>
</template>


<script setup>
import { useDisplay } from 'vuetify'

const route = useRoute()
const tab = ref(null)
const { mdAndUp } = useDisplay()

const { data: info } = await useAsyncData(
  'info',
  () => useHttp(`/api/v1/cables/infrastructures/${route.params.idsupport}`)
)
console.log('INFO', info)
</script>
