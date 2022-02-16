<template>
  <div>
    <v-tabs center-active grow color="indigo">
      <v-tab>
        {{ $t('display.sensitive-areas') }}
      </v-tab>
      <v-tab-item>
        <data-sensitive-area-display :sa-data="saData" />
      </v-tab-item>
      <v-tab> {{ $t('display.mortality-cases') }} </v-tab>
      <v-tab-item>
        <data-mortality-display :mortality-data="mortalityData"
      /></v-tab-item>
      <v-tab> {{ $t('display.poles') }} </v-tab>
      <v-tab-item> <data-pole-display :pole-data="poleData" /></v-tab-item>
      <v-tab> {{ $t('display.segments') }} </v-tab>
      <v-tab-item>
        <data-segment-display :segment-data="segmentData"
      /></v-tab-item>
      <v-tab> {{ $t('display.poles-eqmt') }} </v-tab>
      <v-tab-item> </v-tab-item>
      <v-tab> {{ $t('display.segments-eqmt') }} </v-tab>
      <v-tab-item> </v-tab-item>
    </v-tabs>
  </div>
</template>
<script>
import { FeatureCollection } from 'geojson'
export default {
  name: 'DataDisplay',
  props: {
    saData: FeatureCollection,
    poleData: FeatureCollection,
    segmentData: FeatureCollection,
    mortalityData: FeatureCollection,
  },
  data() {
    return {}
  },
}
</script>

<style>
.v-tab {
  width: 100px;
  background-color: 'indigo';
}

.v-btn {
  width: 80px;
}
</style>
