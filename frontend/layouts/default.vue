
<template>
  <v-app>
    <v-navigation-drawer :mini-variant="miniVariant" clipped app>
      <drawer-menu />
    </v-navigation-drawer>
    <v-app-bar clipped-left app dark elevation="0" color="light-blue darken-4">
      <v-app-bar-nav-icon @click="miniVariant = !miniVariant" />
      <v-toolbar-title v-text="$t('app.app-name')" />
      <v-spacer></v-spacer>
      <div v-if="!$vuetify.breakpoint.mdAndDown">
        {{ $auth.user ? $auth.user.username : $t('app.disconnected') }}
      </div>
      <v-dialog
        v-if="!$auth.loggedIn"
        v-model="dialog"
        :fullscreen="$vuetify.breakpoint.mdAndDown"
        hide-overlay
        transition="dialog-bottom-transition"
        :width="!$vuetify.breakpoint.mdAndDown ? 500 : '100%'"
      >
        <template #activator="{ on, attrs }">
          <v-btn icon class="mr-2" v-bind="attrs" v-on="on">
            <v-icon large>mdi-login</v-icon>
          </v-btn>
        </template>
        <login-component @close-dialog="closeDialog" />
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
    <v-system-bar>
      <v-spacer></v-spacer>
      {{ new Date().getFullYear() }} —
      <strong>{{ $t('app.app-name') }}</strong>
      <a
        href="//github.com/lpoaura/overheadCablesAndBirdlife/"
        target="_blank"
        title="Github project repository"
        ><v-icon class="pl-2">mdi-github</v-icon></a
      >
    </v-system-bar>
    <error-snackbar centered />
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
  data() {
    return {
      miniVariant: true, // small drawer when opening by default
      dialog: false,
    }
  },
  mounted() {
    this.$store.dispatch('mapLayersStore/loadBaseLayers')
  },
  methods: {
    closeDialog() {
      console.log('close from parent')
      this.dialog = false
    },
    /**
     * Logout user and redirect to welcome page
     */
    logout() {
      this.$auth.logout()
    },
  },
}
</script>
