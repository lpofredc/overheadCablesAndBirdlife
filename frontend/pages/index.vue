<template>
  <div>
    <v-row justify="center" align="center">
      <v-col cols="12" sm="8" md="6">
        <v-card class="logo py-4 d-flex justify-center">
          <welcome-component />
        </v-card>
      </v-col>
    </v-row>
    <v-row v-if="!$auth.loggedIn">
      <login-component />
    </v-row>
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
}
</script>
