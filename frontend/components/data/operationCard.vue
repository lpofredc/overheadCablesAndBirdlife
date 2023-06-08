<template>
  <v-card class="my-2">
    <v-card-title>
      {{ $t('display.operation') }}
      <v-spacer />
      <v-btn
        icon="mdi-pencil"
        @click="$router.push(`/supports/21/operation/${props.operation.id}`)"
       />
    </v-card-title>
    <v-card-subtitle>
      {{ $t('operation.last-one') }}{{ props.operation.date }}
    </v-card-subtitle><v-card-text>
      <p>
        <span class="font-weight-bold">{{ $t('operation.type') }}</span>
        {{ props.operation.operation_type.label }}
      </p>
      <p>
        <span class="font-weight-bold">{{ $t('operation.eqmt-type') }}</span>
        <v-chip v-for="et in props.operation.eqmt_type" :key="et.id">
          {{
            et.label
          }}
        </v-chip>
      </p>
      <p>
        <span class="font-weight-bold">{{ $t('app.remark') }}</span>
        {{ props.operation.remark }}
      </p>
    </v-card-text>
  </v-card>
</template>

<script setup lang="ts">

const props = defineProps(['operation'])
console.log('OPERATION', props.operation)
</script>
