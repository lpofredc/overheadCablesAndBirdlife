import { Feature } from 'geojson'
<template>
  <v-container>
    <h1>{{ $t('display.support') }} {{ data.properties.owner.label }}</h1>
    {{ data.properties.actions_infrastructure }}
    <fieldset>
      <legend class="mx-3 px-1">Info Support</legend>
      <h4>réseau: {{ data.properties.owner.label }}</h4>
      <v-container v-for="(ga, index) in data.properties.geo_area" :key="index">
        <h4>Zone Administrative {{ ga.name }}</h4></v-container
      >
      <v-container
        v-for="(sa, index) in data.properties.sensitive_area.features"
        :key="index"
      >
        <h4>Zone Sensible {{ sa.name }}</h4></v-container
      >
    </fieldset>
    <fieldset
      v-for="(infrst, index) in data.properties.actions_infrastructure"
      :key="index"
    >
      <legend class="mx-3 px-1">Info Diagnostic Courant</legend>
      <h4>date: {{ infrst.date }}</h4>
      <h4>remarque: {{ infrst.remark }}</h4>
      <h4>neutralizé: {{ infrst.neutralized }}</h4>
      <h4>condition: {{ infrst.condition.label }}</h4>
      <h4>à isoler: {{ infrst.isolation_advice }}</h4>
      <h4>rendre dissuasif: {{ infrst.dissuasion_advice }}</h4>
      <h4>rendre attractif: {{ infrst.attraction_advice }}</h4>
      <h4>attractivité: {{ infrst.pole_attractivity.label }}</h4>
      <h4>dangerosité: {{ infrst.pole_dangerousness.label }}</h4>
    </fieldset>
  </v-container>
</template>

<script lang="ts">
import { Feature } from 'geojson'

export default {
  name: 'SupportDetailComponent',
  props: { data: { type: Object as () => Feature, default: null } },
  data() {
    return {
      lastDiag: null,
      lastOp: null,
      previousActions: [],
    }
  },
  mounted() {
    if (this.data.properties) {
      // Gather last Diagnosis (field last=True)
      this.lastDiag = this.data.properties.actions_infrastructure.find(
        (action) => action.resourcetype === 'Diagnosis' && action.last
      )
      // Gather last Operation (field last=True)
      this.lastOp = this.data.properties.actions_infrastructure.find(
        (action) => action.resourcetype === 'Operation' && action.last
      )
      // Gather all older actions (Diagnosis and Operations) with field last=False
      this.previousActions = this.data.properties.actions_infrastructure.filter(
        (action) => !action.last
      )
    }
  },
}
</script>
