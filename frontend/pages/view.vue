<template>
  <v-container class="fill-height pa-0">
    <v-row v-if="mdAndUp" class="fill-height">
      <v-col class="pr-0 pt-0 pb-0">
        <!-- <ClientOnly fallback-tag="span" fallback="Loading comments...">
            <map-component :edit-mode="false" />
          </ClientOnly> -->
      </v-col>
      <v-col class="pa-0">
        <display-component />
      </v-col>
    </v-row>

    <template v-if="!mdAndUp">
      <v-tabs v-model="tab" align-tabs="title" fixed-tabs>
        <v-tab> {{ $t('app.map') }} </v-tab>
        <v-tab> {{ $t('app.data') }} </v-tab>
      </v-tabs>

      <v-tabs-items v-model="tab" class="fill-height">
        <v-tab-item>
          <!-- <ClientOnly fallback-tag="span" fallback="Loading comments...">
            <map-component :edit-mode="false" />
          </ClientOnly> -->
        </v-tab-item>
        <v-tab-item>
          <display-component />
        </v-tab-item>
      </v-tabs-items>
    </template>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import { useDisplay } from 'vuetify'

definePageMeta({
  auth: true,
});

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
