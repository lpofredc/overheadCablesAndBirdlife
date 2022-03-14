<template>
  <div style="height: 90vh" class="overflow-auto">
    <v-form ref="form" v-model="formValid" class="text-center">
      <h1>{{ $t('point.new_pole') }}</h1>
      <!-- Filedset COORDINATES -->
      <v-container>
        <fieldset class="d-flex justify-space-around flex-wrap ma-2">
          <legend class="mx-3 px-1">{{ $t('forms.coordinates') }}</legend>
          <v-text-field
            ref="lat"
            v-model="lat"
            :label="$t('point.latitude')"
            :disabled="!manualChange"
            type="number"
            :rules="[rules.requiredOrNotValid, rules.latRange]"
            required
            hide-spin-buttons
            class="shrink mx-5"
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
            class="shrink mx-5"
          />
          <v-checkbox
            v-model="manualChange"
            dense
            :label="$t('point.manual-hadling')"
            class="mx-5"
          ></v-checkbox>
        </fieldset>
        <!-- Filedset GENERAL INFORMATION -->
        <fieldset class="d-flex justify-space-around flex-wrap ma-2">
          <legend class="mx-3 px-1">{{ $t('forms.general') }}</legend>
          <v-container
            class="
              d-flex
              justify-space-around
              flex-sm-row flex-column
              align-center
              flex-wrap
              mx-2
            "
          >
            <v-container
              class="d-flex justify-space-around flex-wrap ma-0 pa-0"
            >
              <v-select
                v-model="owner"
                :items="networkOwners"
                item-text="label"
                item-value="id"
                :rules="[rules.required]"
                :label="$t('point.network')"
                required
                class="shrink mx-10 my-4"
              >
              </v-select>
              <v-menu
                :close-on-content-click="false"
                transition="scale-transition"
                offset-y
                max-width="290px"
                min-width="auto"
              >
                <template #activator="{ on, attrs }">
                  <v-text-field
                    v-model="createDate"
                    :label="$t('forms.datecreate')"
                    persistent-hint
                    prepend-icon="mdi-calendar"
                    readonly
                    class="shrink mx-10 my-4"
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="createDate"
                  no-title
                ></v-date-picker> </v-menu
            ></v-container>
            <v-container
              class="d-flex justify-space-around flex-wrap ma-0 pa-0"
            >
              <v-select
                v-model="poleDesc"
                :items="poleTypes"
                item-text="label"
                item-value="id"
                :rules="[rules.required]"
                hide-selected
                :label="$t('point.poleType')"
                multiple
                deletable-chips
                small-chips
                class="poletypes shrink mx-10 my-4"
              ></v-select>
              <v-select
                v-model="poleCondition"
                :items="conditions"
                item-text="label"
                item-value="id"
                :rules="[rules.required]"
                :label="$t('point.condition')"
                class="shrink mx-10 my-4"
              ></v-select></v-container
            ><v-textarea
              v-model="remark"
              clearable
              clear-icon="mdi-close-circle"
              :label="$t('point.remark')"
              :rules="[rules.textLength]"
              rows="2"
              counter="300"
              class="ma-2 px-5"
            ></v-textarea>
            <v-container
              class="d-flex justify-space-around flex-wrap ma-0 pa-0"
            >
              <v-checkbox
                v-model="neutralized"
                :label="$t('point.neutralized')"
                dense
                class="shrink mx-10 my-4"
              ></v-checkbox>
            </v-container>
          </v-container>
        </fieldset>
        <!-- Filedset RISK ASSESSMENT -->

        <fieldset class="d-flex justify-space-around flex-wrap mx-2">
          <legend class="mx-3 px-1">{{ $t('point.advice') }}</legend>
          <v-container class="d-flex justify-space-around flex-wrap ma-0 pa-0"
            ><v-select
              v-model="attractiveness"
              :items="riskLevels"
              item-text="label"
              item-value="id"
              :rules="[rules.required]"
              :label="$t('point.attractiveness')"
              class="shrink mx-5"
            ></v-select>
            <v-select
              v-model="dangerousness"
              :items="riskLevels"
              item-text="label"
              item-value="id"
              :rules="[rules.required]"
              :label="$t('point.dangerousness')"
              class="shrink mx-5"
            ></v-select></v-container
          ><v-container class="d-flex justify-space-around flex-wrap ma-0 pa-0">
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
            ></v-checkbox>
          </v-container>
        </fieldset>

        <fieldset class="d-flex justify-space-around flex-wrap mx-2">
          <legend class="mx-3 px-1">
            {{ $t('point.pictures') }}
          </legend>
          <utils-picture-component ref="upc" /></fieldset
      ></v-container>
      <v-container>
        <v-row class="justify-space-around mb-2">
          <v-btn @click="back">{{ $t('point.cancel') }}</v-btn>
          <v-btn @click="submit">{{ $t('point.valid') }}</v-btn></v-row
        ></v-container
      >
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
      createDate: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
        .toISOString()
        .substr(0, 10),
      dangerousness: 8, // null,
      dissuadAdv: false,
      isolAdv: false,
      neutralized: false,
      owner: 1, // null,
      poleCondition: 6, // null,
      poleDesc: [],
      remark: null,
      // rules for form validation
      rules: {
        required: (v) => !!v || this.$t('valid.required'),
        requiredOrNotValid: (v) =>
          !!v || this.$t('valid.required_or_not_valid'),
        latRange: (v) =>
          (v >= 40 && v <= 52) || `${this.$t('valid.range')}40 : 52`,
        lngRange: (v) =>
          (v >= -20 && v <= 20) || `${this.$t('valid.range')}-20 : 20`,
        textLength: (v) =>
          (v || '').length <= 300 || `${this.$t('valid.length')}: 300`,
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
    // get back if cancel Point creation. "newPointCoord" reinitialized with lat and lng set to null
    back() {
      this.$store.commit('pointStore/add', { lat: null, lng: null })
      this.$router.back()
    },
    /**
     * submit(): Method to submit the form
     */
    async submit() {
      if (this.$refs.form.validate()) {
        // try create new Pole (Point infrastructure)
        let newPole = null
        const mediaIdList = []
        try {
          // create Point
          const ptData = {}
          ptData.geom = {
            type: 'Point',
            coordinates: [this.lng, this.lat],
          }
          ptData.owner_id = this.owner
          newPole = await this.$axios.$post('cables/points/', ptData)
        } catch (err) {
          const error = {}
          error.code = errorCodes.create_point.code
          error.msg = $nuxt.$t(`error.${errorCodes.create_point.msg}`)
          // set error message to errorStore and triggers message display through "err" watcher in
          // error-snackbar component
          this.$store.commit('errorStore/setError', error)
          this.$router.push('/view')
        }
        // new Pole is successfully created
        if (newPole) {
          // try save each picture (if any) in database
          this.$refs.upc.imgFileObject.forEach(async (img) => {
            try {
              const formData = new FormData()
              formData.append('storage', img)
              // TODO get true date and other form fields
              formData.append('date', '2022-01-01')
              const newImg = await this.$axios.$post('media/', formData, {
                headers: {
                  accept: 'application/json',
                  'Content-Type': 'multipart/form-data',
                },
              })
              mediaIdList.push(newImg.id)
              // Error handling for each picture. An error for one picture do not prevent other
              // pictures be saved
            } catch (_err) {
              const error = {}
              error.code = errorCodes.img_sending.code
              error.msg = $nuxt.$t(`error.${errorCodes.img_sending.msg}`)
              // set error message to errorStore and triggers message display through "err" watcher in
              // error-snackbar component
              this.$store.commit('errorStore/setError', error)
            }
          })
          // TODO: to be completed from here
          // try create Diagnosis
          try {
            const diagData = {}
            diagData.infrastructure = newPole.properties.id
            diagData.date = this.createDate
            diagData.remark = this.remark
            diagData.neutralized = this.neutralized
            diagData.condition_id = this.poleCondition
            diagData.isolation_advice = this.isolAdv
            diagData.dissuasion_advice = this.dissuadAdv
            diagData.attraction_advice = this.attractAdv
            diagData.pole_type_id = this.poleDesc
            diagData.pole_attractivity_id = this.attractiveness
            diagData.pole_dangerousness_id = this.dangerousness
            diagData.media_id = mediaIdList
            await this.$axios.$post('cables/diagnosis/', diagData)
            this.$router.push('/view')
          } catch (_err) {
            // $nuxt.error({
            //   statusCode: errorCodes.create_pole.code,
            //   message:
            //     `Error ${errorCodes.create_pole.code}: ` +
            //     $nuxt.$t(`error.${errorCodes.create_pole.msg}`),
            // })
          }
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

.v-text-field,
.v-select,
.v-checkbox {
  width: 200px;
}

.poletypes {
  width: 300px;
}

.v-textarea {
  min-width: 400px;
}
</style>
