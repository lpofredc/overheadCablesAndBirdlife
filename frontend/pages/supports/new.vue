<template>
  <v-layout>
    <v-container fill-height fluid class="pa-0">

      <v-row class="fill-height">
        <v-col cols="6" class="pr-0 pt-0 pb-0">
          <map-component :edit-mode="true" mode="point" />
        </v-col>
        <v-col cols="6" class="pa-0" style="background-color: red">
          <form-point-component />
        </v-col>
      </v-row>
      <!-- <v-tabs  fixed-tabs bg-color="indigo">
      <v-tab> {{ $t('app.map') }} </v-tab>
      <v-tab-item>
        <map-component :edit-mode="true" mode="point" />
      </v-tab-item>
      <v-tab> {{ $t('app.data') }} </v-tab>
      <v-tab-item>
        <form-point-component />
      </v-tab-item>
    </v-tabs> -->
    </v-container>
  </v-layout>
</template>

<script>
// import { useDisplay } from 'vuetify'

// const {lgAndUp, mdAndDown} = useDisplay()
</script>
