<template>
  <v-sheet color="grey-lighten-4" class="pa-4">
    <v-avatar class="mb-4" color="grey-darken-1" size="64" :image="$auth.user?.avatar"></v-avatar>
    <div>{{ $auth.user?.username || "Not connected" }}</div>
  </v-sheet>

  <v-divider></v-divider>

  <v-list>
    <v-list-item v-for="[icon, text, url] in links" :key="icon" link :to="url">
      <template v-slot:prepend>
        <v-icon>{{ icon }}</v-icon>
      </template>

      <v-list-item-title>{{ text }}</v-list-item-title>
    </v-list-item>
    <v-list-item link to="/account/login">
      <template v-slot:prepend>
        <v-icon icon="mdi-login"></v-icon>
      </template>

      <v-list-item-title>login</v-list-item-title>
    </v-list-item>
  </v-list>
</template>
<script setup>

const $auth = useAuth()
const { t } = useI18n()
useRouter()
const links = ref([
  ["mdi-home", t('login.home_page'), "/"],
  ["mdi-map-search", t('login.application'), "/view"],
  ["mdi-cogs", t('login.admin'), "/admin"],
]);
</script>
