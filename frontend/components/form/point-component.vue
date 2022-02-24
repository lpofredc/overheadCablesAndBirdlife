<template>
  <v-form class="text-center" action="test">
    <h1>{{ $t('infrstr.new_pole') }}</h1>
    <v-row>
      <v-col>
        <form action=""></form>
        <v-text-field
          ref="lat"
          v-model="lat"
          :label="$t('infrstr.latitude')"
          :disabled="!manualChange"
          type="number"
          :rules="[latRule]"
          required
          hide-spin-buttons
        />
      </v-col>
      <v-col>
        <v-text-field
          ref="lng"
          v-model="lng"
          :label="$t('infrstr.longitude')"
          :disabled="!manualChange"
          type="number"
          :rules="[lngRule]"
          required
          hide-spin-buttons
        />
      </v-col>
    </v-row>
    <v-row>
      <v-checkbox
        v-model="manualChange"
        :label="$t('infrstr.manual-hadling')"
      ></v-checkbox>
    </v-row>
    <v-select
      :items="networkOwners"
      item-text="label"
      item-value="id"
      :label="$t('infrstr.network')"
    ></v-select>

    <v-btn @click.stop="back">{{ $t('app.cancel') }}</v-btn>
  </v-form>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'PointComponent',
  data() {
    return {
      manualChange: false,
      latRule: (v) => {
        if (!isNaN(parseFloat(v)) && v >= 40 && v <= 52) return true
        return 'Number has to be between 40 and 52'
      },
      lngRule: (v) => {
        if (!isNaN(parseFloat(v)) && v >= -20 && v <= 22) return true
        return 'Number has to be between -20 and 22'
      },
    }
  },
  computed: {
    /**
     * Getter and Setter for "lat" value.
     * This latitude value is bind v-text-field "lat", and linked with latitude of the LMarker
     * from map-component.
     * When value is commited, it is detected by map-component.vue
     */
    lat: {
      get() {
        return this.newPoint ? this.newPoint.lat : null // avoid bug if newPoint undefined
      },
      // on change in v-text-field, value is set to store.
      set(newVal) {
        if (this.$refs.lat.validate()) {
          this.$store.commit('pointStore/add', { lat: newVal, lng: this.lng })
        } else {
          this.$store.commit('pointStore/add', { lat: null, lng: this.lng })
        }
      },
    },
    /**
     * Getter and Setter for "lng" value.
     * This longitude value is bind v-text-field "lng", and linked with longitude of the LMarker
     * from map-component.
     * When value is commited, it is detected by map-component.vue
     */
    lng: {
      get() {
        return this.newPoint ? this.newPoint.lng : null // avoid bug if newPoint undefined
      },
      // on change in v-text-field, value is set to store.
      set(newVal) {
        if (this.$refs.lng.validate()) {
          this.$store.commit('pointStore/add', { lat: this.lat, lng: newVal })
        } else
          this.$store.commit('pointStore/add', { lat: this.lat, lng: null })
      },
    },
    // Get values from store
    ...mapGetters({
      newPoint: 'pointStore/newCoord',
      networkOwners: 'nomenclaturesStore/getOwners',
    }),
  },
  methods: {
    // get back if cancel Point creation. "newCoord" reinitialized withlat and lng set to null.
    back() {
      this.$store.commit('pointStore/add', { lat: null, lng: null })
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
