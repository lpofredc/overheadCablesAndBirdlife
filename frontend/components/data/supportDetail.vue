<template>
  <div>
    <v-card>
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

            <v-chip v-for="sa in data.properties.sensitive_area" :key="sa.id">
              {{ sa.name }}
            </v-chip>
          </v-card-text>
        </v-card>
        <data-diagnosis-card :diagnosis="lastDiag" />
        <data-operation-card v-if="lastOp" :operation="lastOp" />
        <v-card
          ><v-card-title v-if="previousActions.length" class="font-weight-bold">
            {{ $t('support.history') }}
          </v-card-title>
          <v-expansion-panels>
            <v-expansion-panel
              v-for="action in previousActions"
              :key="action.id"
            >
              <v-expansion-panel-header>
                {{ action.resourcetype }} - {{ action.date }}
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <data-diagnosis-card
                  v-if="action.resourcetype === 'Diagnosis'"
                  :diagnosis="action"
                /><data-operation-card
                  v-if="action.resourcetype === 'Operation'"
                  :operation="action"
                />
              </v-expansion-panel-content>
            </v-expansion-panel> </v-expansion-panels
        ></v-card> </v-container
    ></v-card>
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
