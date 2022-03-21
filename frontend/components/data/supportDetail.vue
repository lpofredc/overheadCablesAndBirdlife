<template>
  <div>
    <form-pointUpdateComponent v-if="update" />
    <v-card v-if="!update">
      <v-toolbar color="green" dark elevation="0">
        <v-toolbar-title
          >{{ $t('support.support') }} {{ data.properties.owner.label }}
        </v-toolbar-title>
        <v-spacer></v-spacer>

        <v-btn icon @click="$router.back()">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-toolbar>

      <!-- <v-btn icon @click="update = true"> -->
      <v-btn icon @click="$router.push('/supports/21/diagnosis/64')">
        <v-icon color="orange">mdi-pencil</v-icon>
      </v-btn>

      {{ lastDiag.date }}
      <v-container>
        <h1>{{ $t('support.support') }} {{ data.properties.owner.label }}</h1>
        <fieldset>
          <legend class="mx-3 px-1">Info Support</legend>
          <h4>réseau: {{ data.properties.owner.label }}</h4>
          <v-container
            v-for="(ga, index) in data.properties.geo_area"
            :key="index"
          >
            <h4>Zone Administrative {{ ga.name }}</h4></v-container
          >
          <v-container
            v-for="(sa, index) in data.properties.sensitive_area.features"
            :key="index"
          >
            <h4>Zone Sensible {{ sa.name }}</h4></v-container
          >
        </fieldset>
        <fieldset>
          <legend class="mx-3 px-1">Info Diagnostic Courant</legend>
          <v-container>
            <h3>DIAGNOSTICS COURANT</h3>
            <h4>date: {{ lastDiag.date }}</h4>
            <h4>remarque: {{ lastDiag.remark }}</h4>
            <h4>neutralizé: {{ lastDiag.neutralized }}</h4>
            <h4>condition: {{ lastDiag.condition.label }}</h4>
            <h4>à iosler: {{ lastDiag.isolation_advice }}</h4>
            <h4>rendre dissuasif: {{ lastDiag.dissuasion_advice }}</h4>
            <h4>rendre attractif: {{ lastDiag.attraction_advice }}</h4>
            <h4>attractivité: {{ lastDiag.pole_attractivity.label }}</h4>
            <h4>dangerosité: {{ lastDiag.pole_dangerousness.label }}</h4>
          </v-container>
          <v-container v-if="lastOp">
            <h3>OPERATION</h3>
            <h4>date: {{ lastOp.date }}</h4>
            <h4>remarque: {{ lastOp.remark }}</h4>
            <h4>Type d'op: {{ lastOp.operation_type.label }}</h4>
            <v-container v-for="(eqmt, ind) in lastOp.eqmt_type" :key="ind">
              {{ eqmt.label }}
            </v-container>
          </v-container>
        </fieldset>
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
