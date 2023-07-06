<template>
  <v-container fill-height fluid class="pa-0">
    <v-row v-if="lgAndUp" class="fill-height">
      <v-col cols="6" class="pr-0 pt-0 pb-0">
        <map :edit-mode="true" mode="line" />
      </v-col>
      <v-col cols="6" class="pa-0" style="background-color: red">
        <form-line />
      </v-col>
    </v-row>
    <v-tabs v-if="mdAndDown" fixed-tabs bg-color="indigo">
      <v-tab> {{ $t('app.map') }} </v-tab>
      <v-tab-item>
        <map :edit-mode="true" mode="point" />
      </v-tab-item>
      <v-tab> {{ $t('app.data') }} </v-tab>
      <v-tab-item>
        <form-line />
      </v-tab-item>
    </v-tabs>
  </v-container>
</template>

<script setup>
import { useDisplay } from 'vuetify'
definePageMeta({
  auth: true,
});
const { lgAndUp, mdAndDown } = useDisplay()
</script>
