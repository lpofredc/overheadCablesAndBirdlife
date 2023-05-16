<template>
  <v-list nav>
    <v-list-item to="/" :disabled="!$auth.loggedIn">
      <template v-slot:prepend>
        <v-icon icon="mdi-home"></v-icon>
      </template>
      <v-list-item-title>{{ $t('login.home_page') }}</v-list-item-title>
    </v-list-item>
    <v-list-item to="/view" :disabled="!$auth.loggedIn" icon="mdi-map-search">
      <template v-slot:prepend>
        <v-icon icon="mdi-eye"></v-icon>
      </template>
      <v-list-item-title>{{ $t('login.application') }}</v-list-item-title>
    </v-list-item>
    <v-list-item href="/admin" :disabled="!$auth.loggedIn" icon="mdi-cogs">
      <template v-slot:prepend>
        <v-icon icon="mdi-lock"></v-icon>
      </template>
      <v-list-item-title>{{ $t('login.admin') }}</v-list-item-title>
    </v-list-item>
  </v-list>
</template>
<script setup>
const $auth = ref({ loggedIn: true })
</script>
