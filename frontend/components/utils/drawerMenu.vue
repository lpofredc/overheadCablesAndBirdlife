<template>
  <VSheet color="grey-lighten-4" class="pa-4">
    <VAvatar class="mb-4" color="grey-darken-1" size="64" :image="$auth.user?.avatar"></VAvatar>
    <div><a to="/account/">{{ $auth.user?.username || "Not connected" }}</a></div>
  </VSheet>

  <VDivider></VDivider>

  <VList>
    <VListItem v-if="$auth.loggedIn" v-for="[icon, text, url, loggedIn] in links" :key="icon" link :to="url">
      <template v-slot:prepend>
      </template>
      <VListItemTitle>{{ text }}</VListItemTitle>
    </VListItem>
    <VListItem v-if="!$auth.loggedIn" link to="/account/login">
      <template v-slot:prepend>
        <VIcon icon="mdi-login"></VIcon>
      </template>
      <VListItemTitle>login</VListItemTitle>
    </VListItem>
  </VList>
</template>
<script setup>

const $auth = useAuth()
const { t } = useI18n()
useRouter()
const links = ref([
  ['mdi-home', t('login.home_page'), '/', null],
  ['mdi-map-search', t('login.application'), '/view', true],
  ['mdi-cogs', t('login.admin'), '/admin', true]
]);
</script>
