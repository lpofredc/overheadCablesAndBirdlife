
<template>
  <v-app>
    <v-navigation-drawer v-model="drawer">
      <utils-drawer-menu />
    </v-navigation-drawer>
    <v-app-bar elevation="0" color="light-blue-darken-4">
      <v-app-bar-nav-icon @click="drawer = !drawer" />
      <v-toolbar-title>{{ $t('app.app-name') }}</v-toolbar-title>
      <v-spacer />
      <div v-if="!mdAndDown">
        {{ $auth.user ? $auth.user.username : $t('app.signin') }}
      </div>
      <v-dialog v-if="!$auth.loggedIn" v-model="dialog" :fullscreen="mdAndDown" :scrim="false"
        transition="dialog-bottom-transition" :width="!mdAndDown ? 500 : '100%'">
        <template #activator="{ props }">
          <v-btn icon class="mr-2" v-bind="props">
            <v-icon size="large">
              mdi-login
            </v-icon>
          </v-btn>
        </template>
        <login @close-dialog="closeDialog" />
      </v-dialog>
      <v-btn v-if="$auth.loggedIn" icon class="mr-2" @click="logout">
        <v-icon size="large">
          mdi-logout
        </v-icon>
      </v-btn>
    </v-app-bar>
    <v-main>
      <v-container fluid class="pa-0" fill-height>
        <Nuxt />
      </v-container>
    </v-main>
    <!-- <v-system-bar>
      <v-spacer></v-spacer>
      {{ new Date().getFullYear() }} —
      <strong>{{ $t('app.app-name') }}</strong>
      <a href="//github.com/lpoaura/overheadCablesAndBirdlife/" target="_blank" title="Github project repository"><v-icon
          class="pl-2">mdi-github</v-icon></a>
    </v-system-bar> -->
    <utils-error-snackbar centered />
  </v-app>
</template>

<script setup>
import { ref } from 'vue'
import { useDisplay } from 'vuetify'

const { mdAndDown } = useDisplay()
const drawer = ref(true)
const dialog = ref(false)

</script>
