
<template>
  <v-card>
    <v-app>
      <v-app-bar clipped-left app hide-on-scroll
        ><v-app-bar-nav-icon
          :disabled="!$auth.loggedIn"
          @click.stop="drawer_opened = !drawer_opened"
        />
        <v-toolbar-title v-text="app_name" />
        <v-spacer></v-spacer>

        <!-- TODO Try with $nuxt.isOffline"  -->
        <div :class="$auth.loggedIn ? 'logged' : 'unlogged'">
          {{ $auth.user ? $auth.user.username : $t('app.disconnected') }}
        </div>
        <v-btn v-if="$auth.loggedIn" icon class="mr -2" @click.stop="logout">
          <v-icon large :color="$auth.loggedIn ? 'red' : 'success'"
            >mdi-logout</v-icon
          >
        </v-btn>
      </v-app-bar>
      <v-navigation-drawer
        v-if="openDrawer()"
        :mini-variant="miniVariant"
        clipped
        app
      >
        <v-btn fixed right icon @click.stop="miniVariant = !miniVariant">
          <v-icon
            >mdi-{{ `chevron-${miniVariant ? 'right' : 'left'}` }}</v-icon
          ></v-btn
        >
        <drawer-menu /></v-navigation-drawer
      ><v-main>
        <Nuxt />
      </v-main>
    </v-app>
  </v-card>
</template>

<script>
export default {
  name: 'DefaultLayout',
  data() {
    return {
      app_name: 'Overhead Cables & BirdLife',
      drawer_opened: true, // drawer closed by default
      miniVariant: true, // wide drawer when opening by default
    }
  },
  methods: {
    openDrawer() {
      return this.$auth.loggedIn ? this.drawer_opened : false
    },
    logout() {
      this.$auth.logout()
      this.$store.$router.push('/login')
    },
  },
}
</script>
