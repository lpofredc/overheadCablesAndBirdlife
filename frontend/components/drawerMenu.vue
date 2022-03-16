<template>
  <v-list dense nav>
    <v-list-item to="/" :disabled="!$auth.loggedIn">
      <v-list-item-icon>
        <v-icon>mdi-home</v-icon>
      </v-list-item-icon>

      <v-list-item-content>
        <v-list-item-title>{{ $t('login.home_page') }}</v-list-item-title>
      </v-list-item-content>
    </v-list-item>
    <!-- <v-list-item to="/" v-if="!$auth.loggedIn">
      <v-list-item-icon>
        <v-icon>mdi-login</v-icon>
      </v-list-item-icon>

      <v-list-item-content>
        <v-list-item-title>{{ $t('login.sign-in') }}</v-list-item-title>
      </v-list-item-content>
    </v-list-item> -->
    <v-list-item to="/view" :disabled="!$auth.loggedIn">
      <v-list-item-icon>
        <v-icon>mdi-map-search</v-icon>
      </v-list-item-icon>

      <v-list-item-content>
        <v-list-item-title>{{ $t('login.application') }}n</v-list-item-title>
      </v-list-item-content>
    </v-list-item>
  </v-list>
</template>
