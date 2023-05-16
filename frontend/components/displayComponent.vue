<template>
  <div class="d-flex align-stretch">
    <v-tabs v-model="tab" grow color="indigo">
      <v-tab value="infra"> {{ $t('display.infrastructures') }} </v-tab>
      <v-tab value="support"> {{ $t('support.supports-eqmt') }} </v-tab>
      <v-tab value="sensitivearea">
        {{ $t('display.sensitive-areas') }}
      </v-tab>
      <v-tab value="mortality"> {{ $t('display.mortality-cases') }} </v-tab>
    </v-tabs>
    <v-window v-model="tab">
      <v-window-item value="infra">
        <data-infrastructure-display />
      </v-window-item>

      <v-window-item value="support">
        <data-equipment-display />
      </v-window-item>

      <v-window-item value="sensitivearea">
        <data-sens-area-display />
      </v-window-item>
      <v-window-item value="mortality">
        <data-mortality-display />
      </v-window-item>
    </v-window>
  </div>
</template>
<script setup>
import { ref } from 'vue'
const tab = ref(null)
</script>

<style>
/* .v-tab {
  width: 100px;
  background-color: 'indigo';
} */
</style>
