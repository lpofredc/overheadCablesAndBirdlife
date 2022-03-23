<template>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <v-flex>
        <v-row justify="center" align="center">
          <v-col cols="12" class="justify-center mb-10" align="center">
            <div class="text-h2 mb--1 text--blue">
              {{ $t('app.app-name') }}
            </div>
          </v-col>
          <v-col cols="12">
            <partners-component />
          </v-col>
        </v-row>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: 'IndexPage',
}
</script>
