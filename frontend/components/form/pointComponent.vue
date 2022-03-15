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
                v-model="pointData.owner_id"
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
                    v-model="diagData.date"
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
                  v-model="diagData.date"
                  no-title
                ></v-date-picker> </v-menu
            ></v-container>
            <v-container
              class="d-flex justify-space-around flex-wrap ma-0 pa-0"
            >
              <v-select
                v-model="diagData.pole_type_id"
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
                v-model="diagData.condition_id"
                :items="conditions"
                item-text="label"
                item-value="id"
                :rules="[rules.required]"
                :label="$t('point.condition')"
                class="shrink mx-10 my-4"
              ></v-select></v-container
            ><v-textarea
              v-model="diagData.remark"
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
                v-model="diagData.neutralized"
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
          <v-container class="d-flex justify-space-around flex-wrap ma-0 pa-0">
            <v-select
              v-model="diagData.pole_attractivity_id"
              :items="riskLevels"
              item-text="label"
              item-value="id"
              :rules="[rules.required]"
              :label="$t('point.attractiveness')"
              class="shrink mx-5"
            ></v-select>
            <v-select
              v-model="diagData.pole_dangerousness_id"
              :items="riskLevels"
              item-text="label"
              item-value="id"
              :rules="[rules.required]"
              :label="$t('point.dangerousness')"
              class="shrink mx-5"
            ></v-select></v-container
          ><v-container class="d-flex justify-space-around flex-wrap ma-0 pa-0">
            <v-checkbox
              v-model="diagData.isolation_advice"
              :label="$t('point.advice_isol')"
              dense
            ></v-checkbox>
            <v-checkbox
              v-model="diagData.dissuasion_advice"
              :label="$t('point.advice_disrupt')"
              dense
            ></v-checkbox>
            <v-checkbox
              v-model="diagData.attraction_advice"
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
      // define data related to Point
      pointData: {
        geom: {
          type: 'Point',
          coordinates: [],
        },
        owner_id: 1, // null,
      },
      // define data related to Diagnosis
      diagData: {
        date: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
          .toISOString()
          .substr(0, 10),
        remark: null,
        pole_type_id: [11, 12], // null,
        neutralized: false,
        condition_id: 6, // null,
        attraction_advice: false,
        dissuasion_advice: false,
        isolation_advice: false,
        pole_attractivity_id: 8, // null
        pole_dangerousness_id: 8, // null
      },
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
    /**
     * back(): Method to get back if cancel Point creation.
     *
     * "newPointCoord" reinitialized with lat and lng set to null
     */
    back() {
      this.$store.commit('pointStore/add', { lat: null, lng: null })
      this.$router.back()
    },

    /**
     * submit(): Method to submit the form to create a Point, then Diagnosis, then Media
     * (pictures) and add these to Diagnosis,
     * .
     *
     * If process fail at any step, all element created before are deleted through error handling
     * process.
     */
    async submit() {
      if (this.formValid) {
        let poleCreated = null
        const mediaIdList = []
        let diagCreated = null
        // Create new Pole (Point infrastructure)
        try {
          this.pointData.geom.coordinates = [this.lng, this.lat]
          // this.pointData.owner_id = this.owner
          poleCreated = await this.$axios.$post(
            'cables/points/',
            this.pointData
          )
        } catch (err) {
          const error = {}
          error.code = errorCodes.create_point.code
          error.msg = $nuxt.$t(`error.${errorCodes.create_point.msg}`)
          // set error message to errorStore and triggers message display through "err" watcher in
          // error-snackbar component
          this.$store.commit('errorStore/setError', error)
          // this.$router.push('/view')
          this.back()
        }
        // new Pole is successfully created
        if (poleCreated) {
          // Create Diagnosis
          try {
            this.diagData.infrastructure = poleCreated.properties.id
            this.diagData.media_id = mediaIdList
            diagCreated = await this.$axios.$post(
              'cables/diagnosis/',
              this.diagData
            )
            this.$router.push('/view')
          } catch (_err) {
            // if no new Diagnosis created
            if (!diagCreated) {
              // if no new Point created, delete it
              if (poleCreated) {
                await this.$axios.$delete(
                  `cables/points/${poleCreated.properties.id}/`
                )
              }
            }
            // Error display
            const error = {}
            error.code = errorCodes.create_pole_diagnosis.code
            error.msg = $nuxt.$t(
              `error.${errorCodes.create_pole_diagnosis.msg}`
            )
            // set error message to errorStore and triggers message display through "err" watcher / in error-snackbar component
            this.$store.commit('errorStore/setError', error)
            // this.$router.push('/view')
            this.back()
          }

          if (diagData) {
            // Create all Media before continuing
            await Promise.all(
              this.$refs.upc.imgFileObject.map(async (img) => {
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
                  mediaIdList.push(newImg.id) // set Media id to mediaIdList
                } catch (_err) {
                  const error = {}
                  error.code = errorCodes.img_sending.code
                  error.msg = $nuxt.$t(`error.${errorCodes.img_sending.msg}`)
                  // set error message to errorStore and triggers message display through "err"
                  // watcher in error-snackbar component
                  this.$store.commit('errorStore/setError', error)
                  // this.$router.push('/view')
                  this.back()
                }
              })
            )
            // add Media to Diagnosis
            try {
              await this.$axios.$patch(`cables/diagnosis/${diagData.id}/`, {
                media_id: mediaIdList,
              })
            } catch (_err) {
              // if adding Media failed, delete created Media
              if (mediaIdList.length > 0) {
                mediaIdList.forEach(async (imgId) => {
                  await this.$axios.$delete(`media/${imgId}/`)
                })
              }
              const error = {}
              error.code = errorCodes.img_sending.code
              error.msg = $nuxt.$t(`error.${errorCodes.img_sending.msg}`)
              // set error message to errorStore and triggers message display through "err"
              // watcher in error-snackbar component
              this.$store.commit('errorStore/setError', error)
              // this.$router.push('/view')
              this.back()
            }
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
