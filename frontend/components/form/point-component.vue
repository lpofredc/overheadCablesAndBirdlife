<template>
  <v-form ref="form" v-model="formValid" class="text-center">
    <h1>{{ $t('infrstr.new_pole') }}</h1>
    <v-container>
      <fieldset class="d-flex justify-space-around flex-wrap mx-2">
        <legend class="mx-3 px-1">{{ $t('infrstr.coord') }}</legend>
        <v-text-field
          ref="lat"
          v-model="lat"
          :label="$t('infrstr.latitude')"
          :disabled="!manualChange"
          type="number"
          :rules="[latRule]"
          required
          hide-spin-buttons
          class="mx-5"
        />
        <v-text-field
          ref="lng"
          v-model="lng"
          :label="$t('infrstr.longitude')"
          :disabled="!manualChange"
          type="number"
          :rules="[lngRule]"
          required
          hide-spin-buttons
          class="mx-5"
        />
        <v-checkbox
          v-model="manualChange"
          dense
          :label="$t('infrstr.manual-hadling')"
          class="mx-5"
        ></v-checkbox></fieldset
    ></v-container>
    <v-container>
      <fieldset class="mx-2">
        <legend class="mx-3 px-1">{{ $t('infrstr.description') }}</legend>
        <v-row class="px-4 py-5"
          ><v-col class="col-4">
            <v-row>
              <v-select
                v-model="owner"
                :items="networkOwners"
                item-text="label"
                item-value="id"
                :label="$t('infrstr.network')"
                required
                class="mx-5"
              >
              </v-select
            ></v-row>
            <v-row
              ><v-menu
                :close-on-content-click="false"
                transition="scale-transition"
                offset-y
                max-width="290px"
                min-width="auto"
              >
                <template #activator="{ on, attrs }">
                  <v-text-field
                    v-model="createDate"
                    :label="$t('infrstr.datecreate')"
                    :hint="$t('infrstr.dateformat')"
                    persistent-hint
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="createDate"
                  no-title
                ></v-date-picker> </v-menu
            ></v-row>
            <v-row
              ><v-select
                v-model="poleCondition"
                :items="conditions"
                item-text="label"
                item-value="id"
                :label="$t('infrstr.condition')"
                class="mx-5"
              ></v-select
            ></v-row>
            <v-row>
              <v-checkbox
                v-model="neutralized"
                :label="$t('infrstr.neutralized')"
                dense
                class="mx-5"
              ></v-checkbox></v-row
          ></v-col>

          <v-col class="col-8">
            <v-container
              ><v-textarea
                v-model="remark"
                clearable
                clear-icon="mdi-close-circle"
                :label="$t('infrstr.remark')"
              ></v-textarea></v-container></v-col
        ></v-row></fieldset
    ></v-container>
    <v-container>
      <fieldset class="d-flex justify-space-around flex-wrap mx-2">
        <legend class="mx-3 px-1">{{ $t('infrstr.advice') }}</legend>
        <v-checkbox
          v-model="isolAdv"
          :label="$t('infrstr.advice_isol')"
          dense
        ></v-checkbox>
        <v-checkbox
          v-model="disruptAdv"
          :label="$t('infrstr.advice_disrupt')"
          dense
        ></v-checkbox>
        <v-checkbox
          v-model="attractAdv"
          :label="$t('infrstr.advice_attract')"
          dense
        ></v-checkbox></fieldset
    ></v-container>
    <v-container>
      <fieldset class="d-flex justify-space-around flex-wrap mx-2">
        <legend class="mx-3 px-1">{{ $t('infrstr.features') }}</legend>
        <v-select
          v-model="attractiveness"
          :items="riskLevels"
          item-text="label"
          item-value="id"
          :label="$t('infrstr.attractiveness')"
          class="mx-5"
        ></v-select>
        <v-select
          v-model="dangerousness"
          :items="riskLevels"
          item-text="label"
          item-value="id"
          :label="$t('infrstr.dangerousness')"
          class="mx-5"
        ></v-select></fieldset
    ></v-container>
    <v-container>
      <v-row class="justify-space-around">
        <v-btn @click.stop="back">{{ $t('infrstr.cancel') }}</v-btn>
        <v-btn @click.stop="submit">{{ $t('infrstr.valid') }}</v-btn></v-row
      ></v-container
    >
  </v-form>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'PointComponent',
  data() {
    return {
      newLat: null,
      newLng: null,
      formValid: true,
      manualChange: false,
      attractAdv: false,
      attractiveness: null,
      createDate: null,
      dangerousness: null,
      disruptAdv: false,
      isolAdv: false,
      neutralized: false,
      owner: null,
      poleCondition: null,
      remark: null,
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
      conditions: 'nomenclaturesStore/getConditions',
      networkOwners: 'nomenclaturesStore/getOwners',
      poleTypes: 'nomenclaturesStore/getPoleTypes',
      riskLevels: 'nomenclaturesStore/getRiskLevels',
    }),
  },
  methods: {
    // get back if cancel Point creation. "newCoord" reinitialized withlat and lng set to null.
    back() {
      this.$store.commit('pointStore/add', { lat: null, lng: null })
      this.$router.back()
    },
    async submit() {
      if (this.$refs.form.validate()) {
        try {
          const data = {}
          data.geom = {
            type: 'Point',
            coordinates: [this.lng, this.lat],
          }
          data.owner_id = this.owner
          const result = await this.$axios.$post('cables/points/', data)
          // If no result, Exception is thrown to be capture by catch section below
          if (!result) {
            throw new Exception()
          }
          this.$router.push('/view')
        } catch (_err) {
          $nuxt.error({
            statusCode: errorCodes.create_pole.code,
            message:
              `Error ${errorCodes.create_pole.code}: ` +
              $nuxt.$t(`error.${errorCodes.create_pole.msg}`),
          })
        }
      }
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
