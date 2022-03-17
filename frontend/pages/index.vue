<template>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <v-flex>
        <v-row v-if="!$auth.loggedIn">
          <login-component />
        </v-row>
        <v-row justify="center" align="center">
          <v-col cols="12" sm="8" md="6">
            <welcome-component />
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
