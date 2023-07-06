<template>
  <v-card class="fill-height overflow-auto">
    <v-layout>
      <v-app-bar density="compact" color="blue-grey-lighten-5">
        <v-app-bar-title>
          {{ $t('support.support') }}
          <strong>{{ props.data.properties.owner.label }}</strong>
        </v-app-bar-title>
        <v-spacer />
        <v-chip small :color="lastDiag.neutralized ? 'success' : 'critical'" variant="elevated">{{ lastDiag.neutralized ?
          'Neutralisé' :
          'A neutraliser' }}</v-chip>
        <v-app-bar-nav-icon>
          <v-btn density="compact" icon="mdi-close" @click="$router.back()" />
        </v-app-bar-nav-icon>
      </v-app-bar>
      <v-main class="overflow-y-auto fill-height">
        <v-card-text>
          <v-card class="my-2">
            <v-layout>
              <v-app-bar density="compact" color="blue-grey-lighten-4">
                <v-app-bar-title>Info Support </v-app-bar-title><v-spacer />
                <v-btn density="compact" icon="mdi-pencil" color="orange" @click="$router.push('/search')" />
              </v-app-bar>
              <v-main>
                <v-card-text>
                  <p class="text-strong" v-if="props.data.properties.geo_area.length > 0">
                    Limites administratives
                  </p>

                  <v-chip v-for="(ga, index) in props.data.properties.geo_area" :key="index">
                    {{ ga.name }} ({{ ga.code }})
                  </v-chip>
                  <p v-if="props.data.properties.sensitive_area.length > 0">
                    Zones sensibles
                  </p>

                  <v-chip v-for="sa in props.data.properties.sensitive_area" :key="sa.id">
                    {{ sa.name }} {{ sa.name }}
                  </v-chip>
                </v-card-text>
              </v-main>
            </v-layout>
          </v-card>
          <data-diagnosis-card :diagnosis="lastDiag" />
          <data-operation-card v-if="lastOp" :operation="lastOp" />
          <v-card><v-card-title v-if="previousActions.length" class="font-weight-bold">
              {{ $t('support.history') }}
            </v-card-title>
            <v-expansion-panels>
              <v-expansion-panel v-for="action in previousActions" :key="action.id">
                <v-expansion-panel-header>
                  {{ action.resourcetype }} - {{ action.date }}
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                  <data-diagnosis-card v-if="action.resourcetype === 'Diagnosis'" :diagnosis="action" />
                  <data-operation-card v-if="action.resourcetype === 'Operation'" :operation="action" />
                </v-expansion-panel-content>
              </v-expansion-panel> </v-expansion-panels></v-card>
        </v-card-text>
      </v-main>
    </v-layout>
  </v-card>
</template>

<script setup lang="ts">


const props = defineProps(['data'])

console.log('props.data' , props.data)



const lastDiag = computed(() => {
  return props.data?.properties.actions_infrastructure.find(
        (action: { resourcetype: string; last: boolean }) =>
          action.resourcetype === 'Diagnosis' && action.last
      )
})

const lastOp = computed(() => {
  return props.data?.properties.actions_infrastructure.find(
        (action: { resourcetype: string; last: boolean }) =>
          action.resourcetype === 'Operation' && action.last
      )
})
const previousActions = computed(() => {
  return props.data?.properties.actions_infrastructure.filter(
        (action: { last: boolean }) => !action.last
      )
})

</script>
