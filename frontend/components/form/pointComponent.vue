<template>
  <v-card elevation="0" class="fill-height">
    <v-form
      ref="
    form"
      v-model="formValid"
      class="text-center"
    >
      <v-toolbar color="pink" dark elevation="0">
        <v-toolbar-title>{{ $t('support.new_support') }}</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn icon @click="$router.back()">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-toolbar>
      <v-card-text class="overflow-auto">
        <v-container>
          <v-row>
            <v-col cols="12" class="text-left">
              <strong>{{ $t('forms.coordinates') }}</strong>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="4">
              <v-text-field
                ref="lat"
                v-model="lat"
                :label="$t('support.latitude')"
                :disabled="!manualChange"
                type="number"
                placeholder="Latitude"
                :rules="[rules.requiredOrNotValid, rules.latRange]"
                required
                hide-spin-buttons
                outlined
                dense
              />
            </v-col>

            <v-col cols="12" md="4">
              <v-text-field
                ref="lng"
                v-model="lng"
                :label="$t('support.longitude')"
                :disabled="!manualChange"
                type="number"
                :rules="[rules.requiredOrNotValid, rules.lngRange]"
                required
                hide-spin-buttons
                outlined
                dense
              />
            </v-col>

            <v-col cols="12" md="4">
              <v-checkbox
                v-model="manualChange"
                dense
                :label="$t('support.manual-handling')"
              ></v-checkbox>
            </v-col>
          </v-row>
        </v-container>
        <v-divider></v-divider>
        <v-container>
          <v-row>
            <v-col cols="12" class="text-left">
              <strong>{{ $t('forms.general') }}</strong>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="6">
              <v-select
                v-model="pointData.owner_id"
                :items="networkOwners"
                item-text="label"
                item-value="id"
                :rules="[rules.required]"
                :label="$t('support.network')"
                outlined
                dense
                required
              >
              </v-select>
            </v-col>

            <v-col cols="12" md="6">
              <v-menu
                :close-on-content-click="false"
                transition="scale-transition"
              >
                <template #activator="{ on, attrs }">
                  <v-text-field
                    v-model="diagData.date"
                    :label="$t('forms.datecreate')"
                    persistent-hint
                    prepend-icon="mdi-calendar"
                    readonly
                    outlined
                    dense
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker v-model="diagData.date" no-title></v-date-picker>
              </v-menu>
            </v-col>

            <v-col cols="12">
              <v-autocomplete
                v-model="diagData.pole_type_id"
                :items="poleTypes"
                item-text="label"
                item-value="id"
                :rules="[rules.required]"
                hide-selected
                :label="$t('support.supportType')"
                multiple
                deletable-chips
                small-chips
                outlined
                dense
              ></v-autocomplete>
            </v-col>

            <v-col cols="12" md="8">
              <v-select
                v-model="diagData.condition_id"
                :items="conditions"
                item-text="label"
                item-value="id"
                :rules="[rules.required]"
                :label="$t('support.condition')"
                outlined
                dense
              ></v-select>
            </v-col>

            <v-col cols="12" md="4">
              <v-checkbox
                v-model="diagData.neutralized"
                :label="$t('support.neutralized')"
                dense
              ></v-checkbox>
            </v-col>
            <v-col cols="12">
              <v-textarea
                v-model="diagData.remark"
                clearable
                clear-icon="mdi-close-circle"
                :label="$t('app.remark')"
                :rules="[rules.textLength]"
                rows="2"
                counter="300"
                outlined
                dense
              ></v-textarea>
            </v-col>
          </v-row>
        </v-container>
        <v-divider></v-divider>
        <v-container>
          <v-row>
            <v-col cols="12" class="text-left">
              <strong>{{ $t('support.advice') }}</strong>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="6">
              <v-select
                v-model="diagData.pole_attractivity_id"
                :items="riskLevels"
                item-text="label"
                item-value="id"
                :rules="[rules.required]"
                :label="$t('support.attractiveness')"
                outlined
                dense
              ></v-select>
            </v-col>
            <v-col cols="12" md="6">
              <v-select
                v-model="diagData.pole_dangerousness_id"
                :items="riskLevels"
                item-text="label"
                item-value="id"
                :rules="[rules.required]"
                :label="$t('support.dangerousness')"
                outlined
                dense
              ></v-select>
            </v-col>
            <v-col cols="12" md="4">
              <v-checkbox
                v-model="diagData.isolation_advice"
                :label="$t('support.advice_isol')"
                dense
              ></v-checkbox>
            </v-col>
            <v-col cols="12" md="4">
              <v-checkbox
                v-model="diagData.dissuasion_advice"
                :label="$t('support.advice_disrupt')"
                dense
              ></v-checkbox>
            </v-col>
            <v-col cols="12" md="4">
              <v-checkbox
                v-model="diagData.attraction_advice"
                :label="$t('support.advice_attract')"
                dense
              ></v-checkbox>
            </v-col>
          </v-row>
        </v-container>
        <v-divider></v-divider>
        <v-container>
          <v-row>
            <v-col cols="12" class="text-left">
              <strong>{{ $t('picture.pictures') }}</strong>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <utils-picture-component ref="upc" />
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-row class="justify-space-around mb-2">
          <v-btn @click="back">{{ $t('app.cancel') }}</v-btn>
          <v-btn @click="submit">{{ $t('app.valid') }}</v-btn>
        </v-row>
      </v-card-actions>
    </v-form>
  </v-card>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'PointComponent',
  data() {
    return {
      formValid: true,
      manualChange: false, // boolean to activate manual coordinate change
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
        pole_attractivity_id: null,
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
        this.$store.commit('coordinatesStore/addPointCoord', {
          lat: Number(newVal),
          lng: this.lng,
        })
        // if (this.$refs.lat.validate()) {
        //   this.$store.commit('coordinatesStore/addPointCoord', {
        //     lat: Number(newVal),
        //     lng: this.lng,
        //   })
        // } else {
        //   this.$store.commit('coordinatesStore/addPointCoord', { lat: null, lng: this.lng })
        // }
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
        this.$store.commit('coordinatesStore/addPointCoord', {
          lat: this.lat,
          lng: Number(newVal),
        })
        // if (this.$refs.lng.validate()) {
        //   this.$store.commit('coordinatesStore/addPointCoord', {
        //     lat: this.lat,
        //     lng: Number(newVal),
        //   })
        // } else
        //   this.$store.commit('coordinatesStore/addPointCoord', { lat: this.lat, lng: null })
      },
    },
    // Get values from store
    ...mapGetters({
      newPoint: 'coordinatesStore/newPointCoord',
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
      this.$store.commit('coordinatesStore/addPointCoord', {
        lat: null,
        lng: null,
      })
      this.$router.back()
    },

    /**
     * submit(): Method to submit the form to create a Point, then Diagnosis, then Media
     * (pictures) and add these to Diagnosis,
     * .
     *
     * If process fail at any step, all elements created before are deleted through error handling
     * process.
     */
    async submit() {
      if (this.formValid) {
        let pointCreated = null
        const mediaIdList = []
        let diagCreated = null
        // Create new Pole (Point infrastructure)
        try {
          this.pointData.geom.coordinates = [this.lng, this.lat]
          pointCreated = await this.$axios.$post(
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
        // new Point is successfully created
        if (pointCreated) {
          // Create Diagnosis
          try {
            this.diagData.infrastructure = pointCreated.properties.id
            this.diagData.media_id = mediaIdList
            diagCreated = await this.$axios.$post(
              'cables/diagnosis/',
              this.diagData
            )
            this.$router.push('/view')
          } catch (_err) {
            // if no new Diagnosis created
            if (!diagCreated) {
              // if new Point was created before, delete it
              if (pointCreated) {
                await this.$axios.$delete(
                  `cables/points/${pointCreated.properties.id}/`
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
            this.back()
          }

          if (diagCreated) {
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
              await this.$axios.$patch(`cables/diagnosis/${diagCreated.id}/`, {
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
/* .v-tab {
  width: 100px;
  background-color: 'indigo';
}

.v-btn {
  width: 80px;
}

.v-text-field,
.v-select,
.v-autocomplete,
.v-checkbox {
  width: 200px;
}

.poletypes {
  width: 300px;
}

.v-textarea {
  min-width: 400px;
} */
</style>
