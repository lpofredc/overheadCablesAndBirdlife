
<template>
  <v-app>
    <v-app-bar clipped-left app dark color="light-blue darken-4"
      ><v-app-bar-nav-icon @click.stop="miniVariant = !miniVariant" />
      <v-toolbar-title v-text="app_name" />
      <v-spacer></v-spacer>
      <div>
        {{ $auth.user ? $auth.user.username : $t('app.disconnected') }}
      </div>
      <v-btn v-if="$auth.loggedIn" icon class="mr -2" @click.stop="logout">
        <v-icon large>mdi-logout</v-icon>
      </v-btn>
    </v-app-bar>
    <v-navigation-drawer :mini-variant="miniVariant" clipped app>
      <drawer-menu /></v-navigation-drawer
    ><v-main>
      <Nuxt />
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
