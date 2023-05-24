
<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawer">
      <utils-drawer-menu />
    </v-navigation-drawer>

    <v-app-bar color="light-blue-darken-4">
      <template #image>
        <v-img gradient="to top right, rgba(19,84,100,.7), rgba(19,84,199,.8)" />
      </template>
      <template #prepend>
        <v-app-bar-nav-icon @click="drawer = !drawer" />
      </template>

      <v-toolbar-title>{{ $t('app.app-name') }}</v-toolbar-title>
      <v-spacer />
      <div v-if="!mdAndDown">
        {{ $auth.user ? $auth.user.username : $t('app.disconnected') }}
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
        <login-component @close-dialog="dialog = false" />
      </v-dialog>
      <v-btn v-if="$auth.loggedIn" icon class="mr-2" @click="$auth.logout()">
        <v-icon size="large">
          mdi-logout
        </v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-container class="pa-0 fill-height">
        <NuxtPage />
      </v-container>
    </v-main>
    <!-- <v-system-bar>
      <v-spacer />
      {{ new Date().getFullYear() }} —
      <strong>{{ $t('app.app-name') }}</strong>
      <a href="//github.com/lpoaura/overheadCablesAndBirdlife/" target="_blank" title="Github project repository"><v-icon
          class="pl-2">mdi-github</v-icon></a>
    </v-system-bar> -->
    <utils-error-snackbar centered />
  </v-app>
</template>

<script setup lang="ts">

import { ref, onMounted } from 'vue'
import { useDisplay } from 'vuetify'
import { useMapLayersStore } from './store/mapLayersStore'

const { mdAndDown } = useDisplay()
const drawer = ref(true)
const dialog = ref(false)

const { $auth } = useNuxtApp()

const loadBaseMapLayers = () => {
  const mapLayersStore = useMapLayersStore()
  console.log('STORE', mapLayersStore)
  mapLayersStore.getMapBaseLayers()
}

onMounted(() => {
  loadBaseMapLayers()
})

</script>
