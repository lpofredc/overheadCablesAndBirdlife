<template>
  <div style="height: 90vh" class="overflow-auto">
    <v-form ref="form" v-model="formValid" class="text-center">
      <h1>{{ $t('line.new_segment') }}</h1>
      <v-container>
        <!-- Filedset COORDINATES -->
        <fieldset class="d-flex justify-space-around flex-wrap ma-2">
          <legend class="mx-3 px-1">{{ $t('forms.coordinates') }}</legend>
          <v-container
            v-if="newLineCoord.length === 0"
            class="text-h6 blue--text text--darken-4"
          >
            {{ $t('line.create_line') }}
          </v-container>
          <v-container
            v-for="(pt, index) in newLineCoord"
            :key="index"
            class="d-flex justify-space-around flex-wrap"
          >
            <v-text-field
              :label="$t('point.latitude')"
              :value="pt[1]"
              type="number"
              :rules="[rules.requiredOrNotValid, rules.latRange]"
              required
              hide-spin-buttons
              class="shrink mx-5" />
            <v-text-field
              :label="$t('point.longitude')"
              :value="pt[0]"
              type="number"
              :rules="[rules.requiredOrNotValid, rules.lngRange]"
              required
              hide-spin-buttons
              class="shrink mx-5"
          /></v-container>
          <!-- <v-checkbox
            v-model="manualChange"
            dense
            :label="$t('point.manual-hadling')"
            class="mx-5"
          ></v-checkbox> -->
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
            <v-select
              v-model="lineData.owner_id"
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
              <v-date-picker v-model="diagData.date" no-title></v-date-picker>
            </v-menu>
            <v-checkbox
              v-model="diagData.neutralized"
              :label="$t('point.neutralized')"
              dense
              class="shrink mx-10 my-4"
            ></v-checkbox></v-container
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
        </fieldset>
        <!-- Filedset GENERAL INFORMATION -->
        <fieldset class="d-flex justify-space-around flex-wrap ma-2">
          <legend class="mx-3 px-1">{{ $t('forms.risk_assessment') }}</legend>
          <v-container class="d-flex justify-space-around flex-wrap py-0">
            <v-select
              v-model="diagData.buildIntegRisk"
              :items="riskLevels"
              item-text="label"
              item-value="id"
              :rules="[rules.required]"
              :label="$t('line.buildIntegRisk')"
              class="shrink mx-5 mt-2"
            ></v-select>
            <v-select
              v-model="diagData.movingRisk"
              :items="riskLevels"
              item-text="label"
              item-value="id"
              :rules="[rules.required]"
              :label="$t('line.movingRisk')"
              class="shrink mx-5 mt-2"
            ></v-select
          ></v-container>
          <v-container class="d-flex justify-space-around flex-wrap py-0">
            <v-select
              v-model="diagData.topoIntegRisk"
              :items="riskLevels"
              item-text="label"
              item-value="id"
              :rules="[rules.required]"
              :label="$t('line.topoIntegRisk')"
              class="shrink mx-5 mt-2"
            ></v-select>
            <v-select
              v-model="diagData.vegetIntegRisk"
              :items="riskLevels"
              item-text="label"
              item-value="id"
              :rules="[rules.required]"
              :label="$t('line.vegetIntegRisk')"
              class="shrink mx-5 mt-2"
            ></v-select
          ></v-container>
        </fieldset>
      </v-container>
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
  name: 'LineComponent',
  data() {
    return {
      // form values
      formValid: true,
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

.v-textarea {
  min-width: 500px;
}

.v-chip {
  margin: 2px;
}
</style>
