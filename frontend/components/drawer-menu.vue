<template>
  <v-list dense nav>
    <v-list-item to="/">
      <v-list-item-icon>
        <v-icon>mdi-home</v-icon>
      </v-list-item-icon>

      <v-list-item-content>
        <v-list-item-title>{{ $t('login.home_page') }}</v-list-item-title>
      </v-list-item-content>
    </v-list-item>
    <v-list-item to="login">
      <v-list-item-icon>
        <v-icon>mdi-login</v-icon>
      </v-list-item-icon>

      <v-list-item-content>
        <v-list-item-title>{{ $t('login.sign-in') }}</v-list-item-title>
      </v-list-item-content>
    </v-list-item>
    <v-list-item to="main">
      <v-list-item-icon>
        <v-icon>mdi-map-search</v-icon>
      </v-list-item-icon>

      <v-list-item-content>
        <v-list-item-title>{{ $t('login.application') }}n</v-list-item-title>
      </v-list-item-content>
    </v-list-item>
  </v-list>
</template>
