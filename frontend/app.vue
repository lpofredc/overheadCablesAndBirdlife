
<template>
  <v-app>
    <v-navigation-drawer :rail="miniVariant">
      <utils-drawer-menu />
    </v-navigation-drawer>
    <v-app-bar elevation="0" color="light-blue-darken-4">
      <v-app-bar-nav-icon @click="miniVariant = !miniVariant" />
      <v-toolbar-title>{{ $t('app.app-name') }}</v-toolbar-title>
      <v-spacer />
      <div v-if="!mdAndDown">
        {{ $auth.user ? $auth.user.username : $t('app.disconnected') }}
      </div>
      <v-dialog
        v-if="!$auth.loggedIn"
        v-model="dialog"
        :fullscreen="mdAndDown"
        :scrim="false"
        transition="dialog-bottom-transition"
        :width="!mdAndDown ? 500 : '100%'"
      >
        <template #activator="{ props }">
          <v-btn icon class="mr-2" v-bind="props">
            <v-icon size="large">
              mdi-login
            </v-icon>
          </v-btn>
        </template>
        <login-component @close-dialog="closeDialog" />
      </v-dialog>
      <v-btn v-if="$auth.loggedIn" icon class="mr-2" @click="logout">
        <v-icon size="large">
          mdi-logout
        </v-icon>
      </v-btn>
    </v-app-bar>
    <v-main>
      <v-container fluid class="pa-0" fill-height>
        <NuxtPage />
      </v-container>
    </v-main>
    <v-system-bar>
      <v-spacer />
      {{ new Date().getFullYear() }} —
      <strong>{{ $t('app.app-name') }}</strong>
      <a href="//github.com/lpoaura/overheadCablesAndBirdlife/" target="_blank" title="Github project repository"><v-icon
        class="pl-2"
      >mdi-github</v-icon></a>
    </v-system-bar>
    <utils-error-snackbar centered />
  </v-app>
</template>

<script>

import { useDisplay } from 'vuetify'
import { useMapLayersStore } from './store/mapLayersStore'

export default {
  name: 'DefaultLayout',
  data () {
    return {
      $auth: {
        loggedIn: true,
        user: {
          username: 'John Doe'
        }
      },
      miniVariant: true, // small drawer at opening
      dialog: false
    }
  },
  computed: {
    mdAndDown () {
      const { mdAndDown } = useDisplay()
      return mdAndDown
    }
  },
  mounted () {
    /**
     * Triggers 'loadBaseLayers' action in mapLayersStore
     */
    // this.$store.dispatch('mapLayersStore/loadBaseLayers')
    this.loadBaseMapLayers()
  },
  methods: {
    /**
     * closeDialog(): Method that close the dialog
     */
    closeDialog () {
      this.dialog = false
    },
    /**
     * logout(): Method that logs out user by calling $auth logout meethod user and redirect to
     *  welcome page due to nuxt.config.js configuration
     */
    logout () {
      // this.$auth.logout()
    },
    loadBaseMapLayers () {
      const mapLayersStore = useMapLayersStore()
      console.log('STORE', mapLayersStore)
      mapLayersStore.loadBaseLayers()
    }
  }
}
</script>
