<template>
  <div style="height: 90vh" class="overflow-auto">
    <v-form ref="form" v-model="formValid" class="text-center">
      <h1>{{ $t('line.new_segment') }}</h1>
      <!-- <v-container>
      <fieldset class="d-flex justify-space-around flex-wrap mx-2">
        <legend class="mx-3 px-1">{{ $t('point.coord') }}</legend>
        <v-text-field
          ref="lat"
          v-model="lat"
          :label="$t('point.latitude')"
          :disabled="!manualChange"
          type="number"
          :rules="[rules.requiredOrNotValid, rules.latRange]"
          required
          hide-spin-buttons
          class="mx-5"
        />
        <v-text-field
          ref="lng"
          v-model="lng"
          :label="$t('point.longitude')"
          :disabled="!manualChange"
          type="number"
          :rules="[rules.requiredOrNotValid, rules.lngRange]"
          required
          hide-spin-buttons
          class="mx-5"
        />
        <v-checkbox
          v-model="manualChange"
          dense
          :label="$t('point.manual-hadling')"
          class="mx-5"
        ></v-checkbox></fieldset
    ></v-container>
    <v-container
      ><fieldset class="mx-2">
        <legend class="mx-3 px-1">{{ $t('point.administrative') }}</legend>
        <v-row class="px-4 py-5">
          <v-spacer></v-spacer>
          <v-select
            v-model="owner"
            :items="networkOwners"
            item-text="label"
            item-value="id"
            :rules="[rules.required]"
            :label="$t('point.network')"
            required
            class="mx-5"
          >
          </v-select>
          <v-spacer></v-spacer
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
                :label="$t('point.datecreate')"
                :hint="$t('point.dateformat')"
                persistent-hint
                prepend-icon="mdi-calendar"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker v-model="createDate" no-title></v-date-picker>
          </v-menu>
          <v-spacer></v-spacer
        ></v-row></fieldset
    ></v-container>
    <v-container>
      <fieldset class="mx-2">
        <legend class="mx-3 px-1">{{ $t('point.description') }}</legend>
        <v-row class="px-4 py-5">
          <v-combobox
            v-model="poleDesc"
            :items="poleTypes"
            item-text="label"
            item-value="id"
            :rules="[rules.required]"
            hide-selected
            label="Search for an option"
            multiple
            small-chips
            deletable-chips
            class="mx-5"
          ></v-combobox
        ></v-row>
        <v-row class="px-4 py-5">
          <v-spacer></v-spacer>
          <v-select
            v-model="poleCondition"
            :items="conditions"
            item-text="label"
            item-value="id"
            :rules="[rules.required]"
            :label="$t('point.condition')"
            class="mx-5"
          ></v-select>

          <v-spacer></v-spacer>
          <v-checkbox
            v-model="neutralized"
            :label="$t('point.neutralized')"
            dense
            class="mx-5"
          ></v-checkbox>
          <v-spacer></v-spacer
        ></v-row>
        <v-row class="px-4 py-5">
          <v-textarea
            v-model="remark"
            clearable
            clear-icon="mdi-close-circle"
            :label="$t('point.remark')"
            class="mx-5"
          ></v-textarea
        ></v-row></fieldset
    ></v-container>
    <v-container>
      <fieldset class="d-flex justify-space-around flex-wrap mx-2">
        <legend class="mx-3 px-1">{{ $t('point.advice') }}</legend>
        <v-checkbox
          v-model="isolAdv"
          :label="$t('point.advice_isol')"
          dense
        ></v-checkbox>
        <v-checkbox
          v-model="dissuadAdv"
          :label="$t('point.advice_disrupt')"
          dense
        ></v-checkbox>
        <v-checkbox
          v-model="attractAdv"
          :label="$t('point.advice_attract')"
          dense
        ></v-checkbox></fieldset
    ></v-container>
    <v-container>
      <fieldset class="d-flex justify-space-around flex-wrap mx-2">
        <legend class="mx-3 px-1">{{ $t('point.features') }}</legend>
        <v-spacer></v-spacer>
        <v-select
          v-model="attractiveness"
          :items="riskLevels"
          item-text="label"
          item-value="id"
          :rules="[rules.required]"
          :label="$t('point.attractiveness')"
          class="mx-5"
        ></v-select
        ><v-spacer></v-spacer>
        <v-select
          v-model="dangerousness"
          :items="riskLevels"
          item-text="label"
          item-value="id"
          :rules="[rules.required]"
          :label="$t('point.dangerousness')"
          class="mx-5"
        ></v-select
        ><v-spacer></v-spacer></fieldset
    ></v-container>
    <v-container>
      <v-row class="justify-space-around">
        <v-btn @click="back">{{ $t('point.cancel') }}</v-btn>
        <v-btn @click="submit">{{ $t('point.valid') }}</v-btn></v-row
      ></v-container
    > -->
    </v-form>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'PointComponent',
  data() {
    return {
      formValid: true,
      manualChange: false,
      // form values
      newLat: null,
      newLng: null,
      attractAdv: false,
      attractiveness: 8, // null,
      createDate: '2022-02-25', // null,
      dangerousness: 8, // null,
      dissuadAdv: false,
      isolAdv: false,
      neutralized: false,
      owner: 1, // null,
      poleCondition: 6, // null,
      poleDesc: null,
      remark: null,
      rules: {
        required: (v) => !!v || this.$t('valid.required'),
        requiredOrNotValid: (v) =>
          !!v || this.$t('valid.required_or_not_valid'),
        latRange: (v) =>
          (v >= 40 && v <= 52) || `${this.$t('valid.range')}40 : 52`,
        lngRange: (v) =>
          (v >= -20 && v <= 20) || `${this.$t('valid.range')}-20 : 20`,
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
          this.$store.commit('pointStore/add', {
            lat: Number(newVal),
            lng: this.lng,
          })
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
          this.$store.commit('pointStore/add', {
            lat: this.lat,
            lng: Number(newVal),
          })
        } else
          this.$store.commit('pointStore/add', { lat: this.lat, lng: null })
      },
    },
    // Get values from store
    ...mapGetters({
      newPoint: 'pointStore/newPointCoord',
      conditions: 'nomenclaturesStore/getConditions',
      networkOwners: 'nomenclaturesStore/getOwners',
      poleTypes: 'nomenclaturesStore/getPoleTypes',
      riskLevels: 'nomenclaturesStore/getRiskLevels',
    }),
  },
  methods: {
    // get back if cancel Point creation. "newPointCoord" reinitialized withlat and lng set to null.
    back() {
      this.$store.commit('pointStore/add', { lat: null, lng: null })
      this.$router.back()
    },
    async submit() {
      if (this.$refs.form.validate()) {
        // try {
        // create Point
        const ptData = {}
        ptData.geom = {
          type: 'Point',
          coordinates: [this.lng, this.lat],
        }
        ptData.owner_id = this.owner
        const newPoint = await this.$axios.$post('cables/points/', ptData)
        // If no newPoint, Exception is thrown to be capture by catch section below
        if (!newPoint) {
          throw new Exception()
        }
        // Create Diagnosis
        const diagData = {}
        diagData.infrastructure = newPoint.properties.id
        diagData.date = this.createDate
        diagData.remark = this.remark
        diagData.neutralized = this.neutralized
        diagData.condition_id = this.poleCondition
        diagData.isolation_advice = this.isolAdv
        diagData.dissuasion_advice = this.dissuadAdv
        diagData.attraction_advice = this.attractAdv
        diagData.pole_type_id = []
        this.poleDesc.forEach((el) => diagData.pole_type_id.push(el.id))
        diagData.pole_attractivity_id = this.attractiveness
        diagData.pole_dangerousness_id = this.dangerousness
        diagData.media_id = []

        const newDiag = await this.$axios.$post('cables/diagnosis/', diagData)
        // If no newDiag, Exception is thrown to be capture by catch section below
        if (!newDiag) {
          throw new Exception()
        }
        this.$router.push('/view')
        // } catch (_err) {
        //   $nuxt.error({
        //     statusCode: errorCodes.create_pole.code,
        //     message:
        //       `Error ${errorCodes.create_pole.code}: ` +
        //       $nuxt.$t(`error.${errorCodes.create_pole.msg}`),
        //   })
        // }
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
