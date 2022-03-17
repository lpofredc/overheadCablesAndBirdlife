
<template>
  <v-app>
    <v-navigation-drawer
      :mini-variant="miniVariant"
      clipped
      mobile-breakpoint="0"
      app
    >
      <drawer-menu />
    </v-navigation-drawer>
    <v-app-bar clipped-left app dark elevation="0" color="light-blue darken-4">
      <v-app-bar-nav-icon @click="miniVariant = !miniVariant" />
      <v-toolbar-title v-text="app_name" />
      <v-spacer></v-spacer>
      <div>
        {{ $auth.user ? $auth.user.username : $t('app.disconnected') }}
      </div>
      <v-dialog v-if="!$auth.loggedIn" v-model="dialog" width="500">
        <template v-slot:activator="{ on, attrs }">
          <v-btn icon class="mr-2" v-bind="attrs" v-on="on">
            <v-icon large>mdi-login</v-icon>
          </v-btn>
        </template>

        <login-component />
      </v-dialog>
      <v-btn v-if="$auth.loggedIn" icon class="mr-2" @click="logout">
        <v-icon large>mdi-logout</v-icon>
      </v-btn>
    </v-app-bar>
    <v-main>
      <v-container fluid class="pa-0" fill-height>
        <Nuxt />
      </v-container>
    </v-main>
    <error-snackbar />
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
  data() {
    return {
      app_name: 'Overhead Cables & BirdLife',
      miniVariant: true, // small drawer when opening by default
    }
  },
  methods: {
    /**
     * Logout user and redirect to welcome page
     */
    logout() {
      this.$auth.logout()
    },
  },
}
</script>
