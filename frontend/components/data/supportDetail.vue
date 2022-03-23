<template>
  <div>
    <form-pointUpdateComponent v-if="update" />
    <v-card v-if="!update">
      <v-toolbar color="green" dark elevation="0">
        <v-toolbar-title
          >{{ $t('support.support') }}
          <strong>{{ data.properties.owner.label }}</strong>
        </v-toolbar-title>
        <v-spacer></v-spacer>

        <v-btn icon @click="$router.back()">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-toolbar>
      <v-card-subtitle>
        Dernier évènement le {{ lastDiag.date }}

        <v-chip small :class="[lastDiag.neutralized ? 'success' : 'error']"
          >{{ lastDiag.neutralized ? 'neutralisé' : 'à neutraliser' }}
        </v-chip></v-card-subtitle
      >

      <v-container>
        <v-card class="my-2">
          <v-card-title
            >Info Support <v-spacer></v-spacer>
            <v-btn icon @click="$router.push('/view')">
              <v-icon color="orange">mdi-pencil</v-icon>
            </v-btn></v-card-title
          >
          <v-card-text>
            <p class="text-strong" v-if="data.properties.geo_area.length > 0">
              Limites administratives
            </p>

            <v-chip
              v-for="(ga, index) in data.properties.geo_area"
              :key="index"
            >
              {{ ga.name }} ({{ ga.code }})
            </v-chip>
            <p v-if="data.properties.sensitive_area.length > 0">
              Zones sensibles
            </p>

            <v-chip
              v-for="(sa, index) in data.properties.sensitive_area"
              :key="index"
            >
              {{ ga.name }}
            </v-chip>
          </v-card-text>
        </v-card>
        <v-card class="my-2">
          <v-card-title>
            Dernier diagnostique&nbsp;
            <span class="text-font-weight">{{ lastDiag.date }}</span>
            <v-spacer></v-spacer>
            <v-btn
              icon
              @click="$router.push(`/supports/21/diagnosis/${lastDiag.id}`)"
            >
              <v-icon color="orange">mdi-pencil</v-icon>
            </v-btn>
          </v-card-title>
          <v-card-text>
            <v-row>
              <v-col> </v-col>
            </v-row>

            <v-chip :class="[lastDiag.isolation_advice ? 'success' : '']"
              >{{ lastDiag.isolation_advice ? 'à ' : 'ne pas ' }}isoler</v-chip
            >
            <v-chip :class="[lastDiag.dissuasion_advice ? 'success' : '']"
              >{{ lastDiag.dissuasion_advice ? '' : 'ne pas ' }}rendre
              dissuasif</v-chip
            >
            <v-chip :class="[lastDiag.attraction_advice ? 'success' : '']"
              >{{ lastDiag.attraction_advice ? '' : 'ne pas ' }}rendre
              attractif</v-chip
            >
            <p>
              <span class="font-weight-bold">Etat</span>
              {{ lastDiag.condition.label }}
            </p>

            <p>
              <span class="font-weight-bold">attractivité</span>
              {{ lastDiag.pole_attractivity.label }}
            </p>
            <p>
              <span class="font-weight-bold">dangerosité</span>
              {{ lastDiag.pole_dangerousness.label }}
            </p>
            <p>
              <span class="font-weight-bold">remarque</span>
              {{ lastDiag.remark }}
            </p>
          </v-card-text>
          <v-container v-if="lastOp">
            <h3>OPERATION</h3>
            <h4>date: {{ lastOp.date }}</h4>
            <h4>remarque: {{ lastOp.remark }}</h4>
            <h4>Type d'op: {{ lastOp.operation_type.label }}</h4>
            <v-container v-for="(eqmt, ind) in lastOp.eqmt_type" :key="ind">
              {{ eqmt.label }}
            </v-container>
          </v-container>
        </v-card>
        <fieldset v-for="(action, index) in previousActions" :key="index">
          <legend class="mx-3 px-1">Autres Actions</legend>
          <v-container v-if="action.resourcetype === 'Diagnosis'">
            <h3>DIAGNOSTICS</h3>
            <h4>date: {{ action.date }}</h4>
            <h4>remarque: {{ action.remark }}</h4>
            <h4>neutralizé: {{ action.neutralized }}</h4>
            <h4>condition: {{ action.condition.label }}</h4>
            <h4>à isoler: {{ action.isolation_advice }}</h4>
            <h4>rendre dissuasif: {{ action.dissuasion_advice }}</h4>
            <h4>rendre attractif: {{ action.attraction_advice }}</h4>
            <h4>attractivité: {{ action.pole_attractivity.label }}</h4>
            <h4>dangerosité: {{ action.pole_dangerousness.label }}</h4>
          </v-container>
          <v-container v-if="action.resourcetype === 'Operation'">
            <h3>OPERATION</h3>
            <h4>date: {{ action.date }}</h4>
            <h4>remarque: {{ action.remark }}</h4>
            <h4>Type d'op: {{ action.operation_type.label }}</h4>
            <v-container v-for="(eqmt, ind) in action.eqmt_type" :key="ind">
              {{ eqmt.label }}
            </v-container>
          </v-container>
        </fieldset>
      </v-container></v-card
    >
  </div>
</template>

<script lang="ts">
import Vue, { PropOptions } from 'vue'
import { Feature } from 'geojson'

export default Vue.extend({
  name: 'SupportDetailComponent',
  props: { data: { type: Object, default: null } as PropOptions<Feature> },
  data() {
    return {
      lastDiag: null,
      lastOp: null,
      previousActions: [],
      update: false,
    }
  },
  created() {
    if (this.data.properties) {
      // Gather last Diagnosis (field last=True)
      this.lastDiag = this.data.properties.actions_infrastructure.find(
        (action: { resourcetype: string; last: boolean }) =>
          action.resourcetype === 'Diagnosis' && action.last
      )
      // Gather last Operation (field last=True)
      this.lastOp = this.data.properties.actions_infrastructure.find(
        (action: { resourcetype: string; last: boolean }) =>
          action.resourcetype === 'Operation' && action.last
      )
      // Gather all older actions (Diagnosis and Operations) with field last=False
      this.previousActions = this.data.properties.actions_infrastructure.filter(
        (action: { last: boolean }) => !action.last
      )
    }
  },
})
</script>
