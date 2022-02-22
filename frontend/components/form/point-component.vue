<template>
  <div>
    {{ newPoint ? newPoint : 'vide' }}
    <!--
      <v-tabs center-active grow color="indigo">
      <v-tab> {{ $t('display.infrastructures') }} </v-tab>
      <v-tab-item> <data-infrastructure-display /></v-tab-item>
      <v-tab> {{ $t('display.poles-eqmt') }} </v-tab>
      <v-tab-item> <data-equipment-display /></v-tab-item>
      <v-tab>
        {{ $t('display.sensitive-areas') }}
      </v-tab>
      <v-tab-item>
        <data-sens-area-display />
      </v-tab-item>
      <v-tab> {{ $t('display.mortality-cases') }} </v-tab>
      <v-tab-item> <data-mortality-display /></v-tab-item>
    </v-tabs>
    -->
    <v-btn @click.stop="back">{{ $t('app.cancel') }}</v-btn>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'PointComponent',
  computed: mapGetters({
    newPoint: 'pointStore/newCoord',
  }),
  methods: {
    back() {
      this.$router.back()
    },
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
