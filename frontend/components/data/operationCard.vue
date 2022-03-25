<template>
  <v-card class="my-2">
    <v-card-title>
      {{ $t('display.operation') }}
      <v-spacer></v-spacer>
      <v-btn
        icon
        @click="$router.push(`/supports/21/operation/${operation.id}`)"
      >
        <v-icon color="orange">mdi-pencil</v-icon>
      </v-btn>
    </v-card-title>
    <v-card-subtitle>
      {{ $t('operation.last-one') }}{{ operation.date }}</v-card-subtitle
    ><v-card-text>
      <p>
        <span class="font-weight-bold">{{ $t('operation.type') }}</span>
        {{ operation.operation_type.label }}
      </p>
      <p>
        <span class="font-weight-bold">{{ $t('operation.eqmt-type') }}</span>
        <v-chip v-for="et in operation.eqmt_type" :key="et.id">{{
          et.label
        }}</v-chip>
      </p>
      <p>
        <span class="font-weight-bold">{{ $t('app.remark') }}</span>
        {{ operation.remark }}
      </p></v-card-text
    ></v-card
  >
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'OperationCardComponent',
  props: { operation: { type: Object, default: null } },
})
</script>
