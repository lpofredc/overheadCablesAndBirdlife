<template>
  <v-list dense nav>
    <v-list-item icon="mdi-home" to="/" :disabled="!$auth.loggedIn">
      <v-list-item-title>{{ $t('login.home_page') }}</v-list-item-title>
    </v-list-item>
    <v-list-item to="/view" :disabled="!$auth.loggedIn" icon="mdi-map-search">
      <v-list-item-title>{{ $t('login.application') }}</v-list-item-title>
    </v-list-item>
    <v-list-item href="/admin" :disabled="!$auth.loggedIn" icon="mdi-cogs">
      <v-list-item-title>{{ $t('login.admin') }}</v-list-item-title>
    </v-list-item>
  </v-list>
</template>
<script setup>
const $auth = ref({ loggedIn: true })
</script>
