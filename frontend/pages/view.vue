<template>
  <v-container class="fill-height pa-0">
    <v-row v-if="mdAndUp" class="fill-height">
      <v-col class="pr-0 pt-0 pb-0">
        <ClientOnly fallback-tag="span" fallback="Loading comments...">
          <map-component :edit-mode="false" />
        </ClientOnly>
      </v-col>
      <v-col class="pa-0">
        <display-component />
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
                <map-component :edit-mode="false" />
              </ClientOnly>
            </v-window-item>
            <v-window-item value="data">
              <display-component />
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
import { ref } from 'vue'
import { useDisplay } from 'vuetify'

definePageMeta({
  auth: true
})

const tab = ref(null)
const { mdAndUp } = useDisplay()

// export default {
//   name: 'ViewComponent',
//   data() {
//     return {
//       tab: null
//     }
//   },
//   mounted() {
//     /**
//      * Call of "loadNomenclatures" action from nomenclaturesStore to load Nomenclatures needed to
//      * get data to set up the application.
//      * Implemented here as authentification needed
//      */
//     this.$store.dispatch('nomenclaturesStore/loadNomenclatures')
//     /**
//      * Call of "addPointCoord" action from coordinatesStore to linitialize newPointCoord at null
//      */
//     this.$store.commit('coordinatesStore/addPointCoord', {
//       lat: null,
//       lng: null
//     })
//   }
// }
</script>
