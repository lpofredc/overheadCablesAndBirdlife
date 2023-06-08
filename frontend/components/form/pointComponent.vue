<template>
  <v-card elevation="0" class="fill-height overflow-auto">
    <v-layout>
      <v-form ref="form" v-model="formValid" class="text-center">
        <v-app-bar color="pink" flat dark density="compact">
          <template v-slot:prepend>
            <v-btn icon="mdi-pencil"></v-btn>
            <v-app-bar-title>{{ modifyDiag ? 'Modifier le' : 'Nouveau' }}
              {{ diagnosis ? 'diagnostic' : $t('support.support') }}
            </v-app-bar-title>
          </template>
          <template v-slot:append>
            <v-btn icon="mdi-close" @click="router.back()" />
          </template>
        </v-app-bar>
        <v-main>
          <v-card-text>
            <v-container v-if="!diagnosis">
              <v-row>
                <v-col cols="12" class="text-left">
                  <strong> {{ $t('forms.general-infrastructure') }}</strong>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" md="4">
                  <v-text-field ref="lat" v-model="lat" :label="$t('support.latitude')" type="number"
                    placeholder="Latitude" :rules="[rules.requiredOrNotValid, rules.latRange]" required hide-spin-buttons
                    outlined dense />
                </v-col>

                <v-col cols="12" md="4">
                  <v-text-field ref="lng" v-model="lng" :label="$t('support.longitude')" type="number"
                    :rules="[rules.requiredOrNotValid, rules.lngRange]" required hide-spin-buttons outlined dense />
                </v-col>
                <v-col cols="12" md="4" v-if="!diagnosis">
                  <v-select v-model="pointData.owner_id" :items="networkOwners" item-title="label" item-value="id"
                    :rules="[rules.required]" :label="$t('support.network')" outlined dense required>
                  </v-select>
                </v-col>
              </v-row>
            </v-container>
            <v-divider></v-divider>
            <v-container>
              <v-row>
                <v-col cols="12" class="text-left">
                  <strong>{{ $t('display.diagnosis') }}</strong>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" md="4" v-if="!support">
                  <v-menu :close-on-content-click="false" transition="scale-transition">
                    <template v-slot:activator="{ props }">
                      <v-text-field v-model="diagData.date" :label="$t('forms.datecreate')" persistent-hint
                        prepend-icon="mdi-calendar" readonly outlined dense v-bind="props"></v-text-field>
                    </template>
                    <v-date-picker v-model="diagData.date" no-title></v-date-picker>
                  </v-menu> </v-col><v-col cols="12" md="4" v-if="!support">
                  <v-select v-model="diagData.condition_id" :items="conditions" item-title="label" item-value="id"
                    :rules="[rules.required]" :label="$t('support.condition')" outlined dense></v-select>
                </v-col>

                <v-col cols="12" md="4" v-if="!support">
                  <v-checkbox v-model="diagData.neutralized" :label="$t('support.neutralized')" dense></v-checkbox>
                </v-col>

                <v-col cols="12" v-if="!support">
                  <v-autocomplete v-model="diagData.pole_type_id" :items="poleTypes" item-title="label" item-value="id"
                    :rules="[rules.required]" hide-selected :label="$t('support.support-type')" multiple deletable-chips
                    small-chips outlined dense></v-autocomplete>
                </v-col>
                <v-col cols="12" md="6">
                  <v-select v-model="diagData.pole_attractivity_id" :items="riskLevels" item-title="label" item-value="id"
                    :rules="[rules.required]" :label="$t('support.attractiveness')" outlined dense></v-select>
                </v-col>
                <v-col cols="12" md="6">
                  <v-select v-model="diagData.pole_dangerousness_id" :items="riskLevels" item-title="label"
                    item-value="id" :rules="[rules.required]" :label="$t('support.dangerousness')" outlined
                    dense></v-select>
                </v-col>
                <v-col cols="12" md="4">
                  <v-checkbox v-model="diagData.isolation_advice" :label="$t('support.advice_isol')" dense></v-checkbox>
                </v-col>
                <v-col cols="12" md="4">
                  <v-checkbox v-model="diagData.dissuasion_advice" :label="$t('support.advice_disrupt')"
                    dense></v-checkbox>
                </v-col>
                <v-col cols="12" md="4">
                  <v-checkbox v-model="diagData.attraction_advice" :label="$t('support.advice_attract')"
                    dense></v-checkbox>
                </v-col>

                <v-col cols="12">
                  <v-textarea v-model="diagData.remark" clearable clear-icon="mdi-close-circle" :label="$t('app.remark')"
                    :rules="[rules.textLength]" rows="2" counter="300" outlined dense></v-textarea>
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
                <v-container>
                  <v-list v-if="diagnosis && modifyDiag">
                    <v-list-item v-for="img in diagnosis.media" :key="img.id">
                      <v-row>
                        <v-col>
                          <v-img :src="img.storage" max-height="100" max-width="166" class="ma-2" />
                        </v-col>

                        <v-col></v-col>
                        <v-col cols="1">
                          <v-icon small color="red">mdi-trash-can</v-icon>
                        </v-col>
                      </v-row>
                    </v-list-item>
                  </v-list></v-container>
              </v-row>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-row class="justify-space-around mb-2">
              <v-btn @click="back">{{ $t('app.cancel') }}</v-btn>
              <v-btn @click="submit">{{ $t('app.valid') }}</v-btn>
            </v-row>
          </v-card-actions>
        </v-main>
      </v-form>
    </v-layout>
  </v-card>
</template>
<script setup lang="ts">
import { mapState } from 'pinia'
import * as errorCodes from '~/static/errorConfig.json'
import { useCoordinatesStore } from '~/store/coordinatesStore'
import { useNomenclaturesStore } from '~/store/nomenclaturesStore'

// // init modules
const { t } = useI18n()
const router = useRouter()
const route = useRoute()

// // init Stores
const coordinatesStore = useCoordinatesStore()
const nomenclaturesStore = useNomenclaturesStore()

// // props
const props = defineProps(['support','diagnosis','operation'])

console.log('diagnosis', props.diagnosis)
console.log('support', props.support)
console.log('operation',props.operation)


const modifyDiag = computed(() => route.query.modifyDiag === 'true' ? true : false)
// data

const form = ref(null) // used to get form ref from "<v-form ref="form">"
const formValid = ref(true)
      // manualChange: false, // boolean to activate manual coordinate change
      // form values
const lat : Ref<null|number> = ref<null | number>(null)
const lng : Ref<null|number>= ref<null | number>(null)
      // To manage Media
const newCreatedMediaIdList : Array<object> = reactive([])
      // define data related to Point
const pointData = reactive({
        geom: {
          type: 'Point',
          coordinates: props.support ? props.support.coordinates : [],
        },
        owner_id: props.support ? props.support.owner_id : null,
      })
      // define data related to Diagnosis
      const diagData = reactive({
        date:
          props.diagnosis && !modifyDiag
            ? props.diagnosis.date
            : new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
              .toISOString()
              .substr(0, 10),
        remark: props.diagnosis ? props.diagnosis.remark : null,
        pole_type_id: props.diagnosis
          ? props.diagnosis.pole_type.map((pt) => pt.id)
          : [],
        neutralized: props.diagnosis ? props.diagnosis.neutralized : false,
        condition_id: props.diagnosis ? props.diagnosis.condition.id : null,
        attraction_advice: props.diagnosis
          ? props.diagnosis.attraction_advice
          : false,
        dissuasion_advice: props.diagnosis
          ? props.diagnosis.dissuasion_advice
          : false,
        isolation_advice: props.diagnosis
          ? props.diagnosis.isolation_advice
          : false,
        pole_attractivity_id: props.diagnosis
          ? props.diagnosis.pole_attractivity.id
          : null,
        pole_dangerousness_id: props.diagnosis
          ? props.diagnosis.pole_dangerousness.id
          : null,
        media_id: props.diagnosis ? props.diagnosis.media.map((m) => m.id) : [],
      })
//       // rules for form validation
      const rules = reactive({
        required: (v) => !!v || t('valid.required'),
        requiredOrNotValid: (v) =>
          v === 0 || !!v || t('valid.required_or_not_valid'),
        latRange: (v) =>
          (v >= 40 && v <= 52) || `${t('valid.range')}40 : 52`,
        lngRange: (v) =>
          (v >= -20 && v <= 20) || `${t('valid.range')}-20 : 20`,
        textLength: (v) =>
          (v || '').length <= 300 || `${t('valid.length')}: 300`,
      })


// Menu items
const poleTypes = computed(() =>  nomenclaturesStore.poleTypeItems)
const networkOwners = computed(() => nomenclaturesStore.ownerItems)
const conditions = computed(() => nomenclaturesStore.conditionItems)
const riskLevels = computed(() => nomenclaturesStore.riskLevelItems)



    // Methods
    const back = () => {
      coordinatesStore.addPointCoord({
        lat: null,
        lng: null,
      })
      router.back()
    }

    /**
     * submit(): Method to submit the form for Point/Diagnosis/Media creation or update
     * .
     *
     * If process fail at any step, all elements created before are deleted through error handling
     * process.
     */
    const submit = async () => {
      if (formValid) {
        // Case of creation of new Point and associated Diagnosis
        if (!props.support && !props.diagnosis) {
          const pointCreated = await createNewPoint()
          // new Point (Support) is successfully created
          if (pointCreated) {
            // Create Diagnosis
            await createNewDiagnosis(pointCreated.properties.id)
          }
          router.push('/view')
        } else if (props.diagnosis && modifyDiag) {
          // Case of update of Diagnosis
          await this.updateDiagnosis()
          router.push(`/supports/${props.diagnosis.infrastructure}`)
        } else if (props.diagnosis && !modifyDiag) {
          // Case of creation of new Diagnosis on existing Support
          await this.addNewDiagnosis()
          router.push(`/supports/${props.diagnosis.infrastructure}`)
        } else if (this.support) {
          // update of existing Point
          const error = {
            code: 0,
            msg: 'Update of Support not implemented yet',
          }
          // set error message to errorStore and triggers message display through "err"
          // watcher in error-snackbar component
          this.$store.commit('errorStore/setError', error)
        }
      }
    }

    /**
     * createNewPoint(): Method that create new Point based on forms data (cf. this.pointData)
     *
     * @return {JSON object} as new Point
     *
     * If process fails, error message is displayed in snackBar through error handling process.
     */
     const createNewPoint = async () => {
      try {
        pointData.geom.coordinates = [lng, lat]
        return await useHttp('cables/points/', 'post', pointData)
      } catch (_err) {
        const error = {}
        error.code = errorCodes.create_point.code
        error.msg = t(`error.${errorCodes.create_point.msg}`)
        // set error message to errorStore and triggers message display through "err" watcher in
        // error-snackbar component
        errorStore.setError(error)
        back()
      }
    }

    /**
     * createNewDiagnosis(): Method that create new Diagnosis based on forms data(cf.this.diagData)
     *
     * @param {Number} infrstr_id id of related Insfrastructure (Point)
     *
     * Error handling: A Diagnosis should be created at time of Infrastructure (Point) creation.
     * If Diagnosis creation fails, related Infrastructure (Point) will be deleted.
     * Related Media will also be deleted in this case.
     * Finally, error message is displayed in snackBar through error handling process.
     */
    const createNewDiagnosis = async (infrstr_id) => {
      // Create Media as selected in component form and get list of Ids of created Media
      const mediaIdList = await createNewMedia()
      try {
        this.diagData.infrastructure = infrstr_id // set Infrastructure (Point) id
        this.diagData.media_id = mediaIdList // set Media id list
        // Create Diagnosis
        return await this.$axios.$post('cables/diagnosis/', this.diagData)
      } catch (_err) {
        // If Diagnosis creation fails, related infrastructure(Point) is deleted
        await this.$axios.$delete(`cables/points/${infrstr_id}/`)
        // If Diagnosis creation fails, related Media created are deleted
        if (this.newCreatedMediaIdList) {
          this.newCreatedMediaIdList.forEach(
            async (media_id) => await this.$axios.$delete(`/media/${media_id}/`)
          )
        }
        // Error display
        const error = {}
        error.code = errorCodes.create_pole_diagnosis.code
        error.msg = $nuxt.$t(`error.${errorCodes.create_pole_diagnosis.msg}`)
        // set error message to errorStore and triggers message display through "err" watcher / in error-snackbar component
        this.$store.commit('errorStore/setError', error)
        this.back()
      }
    }

    /**
     * addNewDiagnosis(): Method that create new Diagnosis based on forms data (cf.this.diagData)
     * on an existing Support
     *
     * Error handling: A Diagnosis should be created at time of Infrastructure (Point) creation.
     * If Diagnosis creation fails, related Infrastructure (Point) will be deleted.
     * Related Media will also be deleted in this case.
     * Finally, error message is displayed in snackBar through error handling process.
     */
    const addNewDiagnosis = async () => {
      // Create Media as selected in component form and get list of Ids of created Media
      console.log(modifyDiag ? 'vrai' : 'faux')
      const mediaIdList = await this.createNewMedia()
      try {
        this.diagData.infrastructure = props.diagnosis.infrastructure // set Infrastructure (Point) id
        this.diagData.media_id = mediaIdList // set Media id list
        // Create Diagnosis
        return await this.$axios.$post('cables/diagnosis/', this.diagData)
      } catch (_err) {
        // If Diagnosis creation fails, related Media created are deleted
        if (this.newCreatedMediaIdList) {
          this.newCreatedMediaIdList.forEach(
            async (media_id) => await this.$axios.$delete(`/media/${media_id}/`)
          )
        }
        // Error display
        const error = {}
        error.code = errorCodes.create_pole_diagnosis.code
        error.msg = $nuxt.$t(`error.${errorCodes.create_pole_diagnosis.msg}`)
        // set error message to errorStore and triggers message display through "err" watcher / in error-snackbar component
        this.$store.commit('errorStore/setError', error)
        this.back()
      }
    }

    /**
     * updateDiagnosis(): Method that update Diagnosis based on forms data (cf.this.diagData)
     *
     * Error handling: If Diagnosis update fails, new created Media will be deleted.
     * Finally, error message is displayed in snackBar through error handling process.
     */
    const updateDiagnosis = async () => {
      // Create new Media as selected in component form and get list of Ids of created Media
      const mediaIdList = await this.createNewMedia()
      try {
        this.diagData.infrastructure = props.diagnosis.infrastructure // set Infrastructure (Point) id
        this.diagData.media_id = mediaIdList // set Media id list
        // Create Diagnosis
        return await this.$axios.$put(
          `cables/diagnosis/${props.diagnosis.id}/`,
          this.diagData
        )
      } catch (_err) {
        // If Diagnosis creation fails, related Media created are deleted
        if (this.newCreatedMediaIdList) {
          this.newCreatedMediaIdList.forEach(
            async (media_id) => await this.$axios.$delete(`/media/${media_id}/`)
          )
        }
        // Error display
        const error = {}
        error.code = errorCodes.update_pole_diagnosis.code
        error.msg = $nuxt.$t(`error.${errorCodes.update_pole_diagnosis.msg}`)
        // set error message to errorStore and triggers message display through "err" watcher / in error-snackbar component
        this.$store.commit('errorStore/setError', error)
        this.back()
      }
    }

    /**
     * createNewMedia(): Method that create new Media based on component forms data and return the
     * list of Ids of created Media
     *
     * @return {Number[]} as new Diagnosis
     *
     * If process fails for at least one Media creation, error message is displayed in snackBar
     * through error handling process. Id of Media for which creation did not fail will be return
     * anyway.
     */
    const createNewMedia = async() => {
      const mediaIdList = modifyDiag ? this.diagData.media_id : []

      // await all Promises be resolved before returning result
      await Promise.all(
        // upc for "util-picture-component": task on each img file of the map
        this.$refs.upc.imgFileObject.map(async (img) => {
          try {
            const formData = new FormData()
            formData.append('storage', img) // fill-in FormData with img file
            // TODO get true date and other form fields below
            formData.append('date', '2022-01-01')
            formData.append('author', 'Bob')
            formData.append('source', 'LPO')
            formData.append('remark', 'Nothing to report')
            // create Media
            const newImg = await this.$axios.$post('media/', formData, {
              headers: {
                accept: 'application/json',
                'Content-Type': 'multipart/form-data',
              },
            })
            mediaIdList.push(newImg.id) // set Media id to mediaIdList
            this.newCreatedMediaIdList.push(newImg.id)
          } catch (_err) {
            const error = {}
            error.code = errorCodes.img_sending.code
            error.msg = $nuxt.$t(`error.${errorCodes.img_sending.msg}`)
            // set error message to errorStore and triggers message display through "err"
            // watcher in error-snackbar component
            this.$store.commit('errorStore/setError', error)
          }
        })
      )
      return mediaIdList
    }


</script>
