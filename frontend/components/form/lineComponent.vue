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
              v-model="pt[1]"
              :label="$t('point.latitude')"
              type="number"
              :rules="[rules.requiredOrNotValid, rules.latRange]"
              required
              hide-spin-buttons
              class="shrink mx-5" />
            <v-text-field
              v-model="pt[0]"
              :label="$t('point.longitude')"
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
              <v-date-picker v-model="createDate" no-title></v-date-picker>
            </v-menu>
            <v-checkbox
              v-model="neutralized"
              :label="$t('point.neutralized')"
              dense
              class="shrink mx-10 my-4"
            ></v-checkbox></v-container
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
        </fieldset>
        <!-- Filedset GENERAL INFORMATION -->
        <fieldset class="d-flex justify-space-around flex-wrap ma-2">
          <legend class="mx-3 px-1">{{ $t('forms.risk_assessment') }}</legend>
          <v-container class="d-flex justify-space-around flex-wrap py-0">
            <v-select
              v-model="buildIntegRisk"
              :items="riskLevels"
              item-text="label"
              item-value="id"
              :rules="[rules.required]"
              :label="$t('line.buildIntegRisk')"
              class="shrink mx-5 mt-2"
            ></v-select>
            <v-select
              v-model="movingRisk"
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
              v-model="topoIntegRisk"
              :items="riskLevels"
              item-text="label"
              item-value="id"
              :rules="[rules.required]"
              :label="$t('line.topoIntegRisk')"
              class="shrink mx-5 mt-2"
            ></v-select>
            <v-select
              v-model="vegetIntegRisk"
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
  name: 'PointComponent',
  data() {
    return {
      // ####################
      // form values
      formValid: true,
      // newLineCoord: [],
      neutralized: false,
      newLineCoord: [
        [1, 45],
        [1, 46],
      ],
      // manualChange: false,
      buildIntegRisk: null,
      movingRisk: null,
      createDate: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
        .toISOString()
        .substr(0, 10),
      owner: null,
      remark: null,
      topoIntegRisk: null,
      vegetIntegRisk: null,
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
      // newLine: 'pointStore/newLineCoord',
      networkOwners: 'nomenclaturesStore/getOwners',
      riskLevels: 'nomenclaturesStore/getRiskLevels',
    }),
  },
  methods: {
    // get back if cancel Line creation. "newLineCoord" reinitialized with at []
    back() {
      // this.$store.commit('pointStore/add', { lat: null, lng: null })
      this.$router.back()
    },
    async submit() {
      if (this.$refs.form.validate()) {
        // // try {
        // create Line
        const lineData = {}
        lineData.geom = {
          type: 'LineString',
          coordinates: this.newLineCoord,
        }
        lineData.owner_id = this.owner
        const newLine = await this.$axios.$post('cables/lines/', lineData)
        // If no newLine, Exception is thrown to be capture by catch section below
        if (!newLine) {
          throw new Exception()
        }
        // Create Diagnosis
        const diagData = {}
        diagData.infrastructure = newLine.properties.id
        diagData.date = this.createDate
        diagData.remark = this.remark
        diagData.neutralized = this.neutralized
        diagData.media_id = []
        diagData.buildIntegRisk = this.buildIntegRisk
        diagData.movingRisk = this.movingRisk
        diagData.topoIntegRisk = this.topoIntegRisk
        diagData.vegetIntegRisk = this.vegetIntegRisk
        const newDiag = await this.$axios.$post('cables/diagnosis/', diagData)
        // If no newDiag, Exception is thrown to be capture by catch section below
        if (!newDiag) {
          throw new Exception()
        }
        // this.$router.push('/view')
        // // } catch (_err) {
        // //   $nuxt.error({
        // //     statusCode: errorCodes.create_pole.code,
        // //     message:
        // //       `Error ${errorCodes.create_pole.code}: ` +
        // //       $nuxt.$t(`error.${errorCodes.create_pole.msg}`),
        // //   })
        // // }
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
