<template>
  <v-card elevation="0" class="fill-height">
    <v-form
      ref="
    form"
      v-model="formValid"
      class="text-center"
    >
      <v-toolbar color="pink" dark elevation="0">
        <v-toolbar-title>{{ $t('line.new_segment') }}</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon @click="$router.back()">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-toolbar>
      <v-card-text class="overflow-auto">
        <!-- Filedset COORDINATES -->
        <!-- <v-container>
         
          <v-row>
            <v-col cols="12" class="text-left">
              <strong>{{ $t('forms.coordinates') }}</strong>
              <v-btn icon @click="manualChange=!manualChange">
          <v-icon>mdi-pen</v-icon>
        </v-btn>
            </v-col>
          </v-row>
          <v-row 
            v-for="(pt, index) in newLineCoord"
            :key="index"
            >
            <v-col cols="12" md="6" >
              <v-text-field
                ref="lat"
                :value="pt[1]"
                :label="$t('support.latitude')"
                :disabled="!manualChange"
                type="number"
                placeholder="Latitude"
                :rules="[rules.requiredOrNotValid, rules.latRange]"
                required
                hide-spin-buttons
                outlined
                dense
                disable
              />
            </v-col>

            <v-col cols="12" md="6">
              <v-text-field
                ref="lng"
                :value="pt[0]"
                :label="$t('support.longitude')"
                :disabled="!manualChange"
                type="number"
                :rules="[rules.requiredOrNotValid, rules.lngRange]"
                required
                hide-spin-buttons
                outlined
                dense
                disable
              />
            </v-col>
          </v-row>
        </v-container> -->

        <!-- Filedset GENERAL INFORMATION -->
        <v-container>
          <v-row>
            <v-col cols="12" class="text-left">
              <strong>{{ $t('forms.general') }}</strong>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="4">
              <v-select
                v-model="lineData.owner_id"
                :items="networkOwners"
                item-text="label"
                item-value="id"
                :rules="[rules.required]"
                :label="$t('support.network')"
                required
                dense
                outlined
              >
              </v-select>
            </v-col>

            <v-col cols="12" md="4">
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
        <!-- Filedset GENERAL INFORMATION -->
        <v-container>
          <v-row>
            <v-col cols="12" class="text-left">
              <strong>{{ $t('forms.risk_assessment') }}</strong>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" lg="3" md="6">
              <v-select
                v-model="diagData.buildIntegRisk"
                :items="riskLevels"
                item-text="label"
                item-value="id"
                :rules="[rules.required]"
                :label="$t('line.buildIntegRisk')"
                outlined
                dense
              ></v-select>
            </v-col>
            <v-col cols="12" lg="3" md="6">
              <v-select
                v-model="diagData.movingRisk"
                :items="riskLevels"
                item-text="label"
                item-value="id"
                :rules="[rules.required]"
                :label="$t('line.movingRisk')"
                outlined
                dense
              ></v-select>
            </v-col>

            <v-col cols="12" lg="3" md="6">
              <v-select
                v-model="diagData.topoIntegRisk"
                :items="riskLevels"
                item-text="label"
                item-value="id"
                :rules="[rules.required]"
                :label="$t('line.topoIntegRisk')"
                outlined
                dense
              ></v-select>
            </v-col>
            <v-col cols="12" lg="3" md="6">
              <v-select
                v-model="diagData.vegetIntegRisk"
                :items="riskLevels"
                item-text="label"
                item-value="id"
                :rules="[rules.required]"
                :label="$t('line.vegetIntegRisk')"
                outlined
                dense
              ></v-select>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-row class="justify-space-around mb-2">
          <v-btn color="error" @click="back">{{ $t('app.cancel') }}</v-btn>
          <v-btn color="success" @click="submit">{{ $t('app.valid') }}</v-btn>
        </v-row>
      </v-card-actions>
    </v-form>
  </v-card>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'LineComponent',
  data() {
    return {
      // form values
      formValid: true,
      manualChange: false,
      // define data related to Point
      lineData: {
        geom: {
          type: 'LineString',
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
        buildIntegRisk: null,
        movingRisk: null,
        topoIntegRisk: null,
        vegetIntegRisk: null,
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
    // Get values from store
    ...mapGetters({
      newLineCoord: 'coordinatesStore/newLineCoord',
      networkOwners: 'nomenclaturesStore/getOwners',
      riskLevels: 'nomenclaturesStore/getRiskLevels',
    }),
  },
  methods: {
    /**
     * back(): Method to get back if cancel Point creation.
     *
     * "newLineCoord" reinitialized with at []
     */
    back() {
      this.$store.commit('coordinatesStore/addLineCoord', [])
      this.$router.back()
    },

    /**
     * submit(): Method to submit the form to create a Line, then Diagnosis
     *
     * TODO Add pictures ["then Media (pictures) and add these to Diagnosis]
     *
     * If process fail at any step, all elements created before are deleted through error handling
     * process.
     */
    async submit() {
      if (this.formValid) {
        let lineCreated = null
        const mediaIdList = []
        let diagCreated = null
        // Create new segment (Line infrastructure)
        try {
          this.lineData.geom.coordinates = this.newLineCoord
          lineCreated = await this.$axios.$post('cables/lines/', this.lineData)
        } catch (err) {
          const error = {}
          error.code = errorCodes.create_line.code
          error.msg = $nuxt.$t(`error.${errorCodes.create_line.msg}`)
          // set error message to errorStore and triggers message display through "err" watcher in
          // error-snackbar component
          this.$store.commit('errorStore/setError', error)
          // this.$router.push('/view')
          this.back()
        }
        // new Line is successfully created
        if (lineCreated) {
          // Create Diagnosis
          try {
            this.diagData.infrastructure = lineCreated.properties.id
            this.diagData.media_id = mediaIdList
            diagCreated = await this.$axios.$post(
              'cables/diagnosis/',
              this.diagData
            )
            this.$router.push('/view')
          } catch (_err) {
            // if no new Diagnosis created
            if (!diagCreated) {
              // if new Line was created before, delete it
              if (lineCreated) {
                await this.$axios.$delete(
                  `cables/lines/${lineCreated.properties.id}/`
                )
              }
            }
            // Error display
            const error = {}
            error.code = errorCodes.create_line_diagnosis.code
            error.msg = $nuxt.$t(
              `error.${errorCodes.create_line_diagnosis.msg}`
            )
            // set error message to errorStore and triggers message display through "err" watcher / in error-snackbar component
            this.$store.commit('errorStore/setError', error)
            this.back()
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

/* .v-text-field,
.v-select,
.v-checkbox {
  width: 200px;
} */

/*
.v-textarea {
  min-width: 500px;
}

.v-chip {
  margin: 2px;
} */
</style>
