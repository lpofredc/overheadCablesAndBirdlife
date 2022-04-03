<template>
  <v-card class="my-2">
    <v-card-title>
      {{ $t('display.diagnosis') }}
      <v-spacer></v-spacer
      ><v-btn
        icon
        @click="
          $router.push({
            path: `/supports/21/diagnosis/${diagnosis.id}`,
            query: { modifyDiag: false },
          })
        "
      >
        <v-icon v-if="diagnosis.last" color="green"
          >mdi-eye-plus-outline</v-icon
        >
      </v-btn>
      <v-btn
        icon
        @click="
          $router.push({
            path: `/supports/21/diagnosis/${diagnosis.id}`,
            query: { modifyDiag: true },
          })
        "
      >
        <v-icon color="orange">mdi-pencil</v-icon>
      </v-btn>
    </v-card-title>
    <v-card-subtitle>
      {{ $t('diagnosis.last-one') }}{{ diagnosis.date }}

      <v-chip small :class="[diagnosis.neutralized ? 'success' : 'error']"
        >{{ diagnosis.neutralized ? 'neutralisé' : 'à neutraliser' }}
      </v-chip></v-card-subtitle
    >

    <v-card-text>
      <p>
        <v-chip :class="[diagnosis.isolation_advice ? 'success' : '']"
          >{{ diagnosis.isolation_advice ? '' : 'ne pas '
          }}{{ $t('diagnosis.isolate') }}</v-chip
        >
        <v-chip :class="[diagnosis.dissuasion_advice ? 'success' : '']"
          >{{ diagnosis.dissuasion_advice ? '' : 'ne pas '
          }}{{ $t('diagnosis.make-dissuasive') }}</v-chip
        >
        <v-chip :class="[diagnosis.attraction_advice ? 'success' : '']"
          >{{ diagnosis.attraction_advice ? '' : 'ne pas '
          }}{{ $t('diagnosis.make-attractive') }}</v-chip
        >
      </p>

      <p>
        <span class="font-weight-bold">{{ $t('support.condition') }}</span>
        {{ diagnosis.condition.label }}
      </p>
      <p>
        <span class="font-weight-bold">{{ $t('support.support-type') }}</span>
        <v-chip v-for="pt in diagnosis.pole_type" :key="pt.id">{{
          pt.label
        }}</v-chip>
      </p>

      <p>
        <span class="font-weight-bold">{{ $t('support.attractiveness') }}</span>
        {{ diagnosis.pole_attractivity.label }}
      </p>
      <p>
        <span class="font-weight-bold">{{ $t('support.dangerousness') }}</span>
        {{ diagnosis.pole_dangerousness.label }}
      </p>
      <p>
        <span class="font-weight-bold">{{ $t('app.remark') }}</span>
        {{ diagnosis.remark }}
      </p>
      <v-list>
        <v-list-item v-for="img in diagnosis.media" :key="img.id">
          <v-row>
            <v-col>
              <v-img
                :src="img.storage"
                max-height="100"
                max-width="166"
                class="ma-2"
              />
            </v-col>
            <!-- <v-col>date: {{ pictDate }}</v-col>   -->
            <v-col></v-col>
            <v-col cols="1">
              <v-icon small color="red">mdi-trash-can</v-icon>
            </v-col>
          </v-row>
        </v-list-item>
      </v-list>
    </v-card-text>
  </v-card>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'DiagnosisCardComponent',
  props: { diagnosis: { type: Object, default: null } },
})
</script>
