<template>
  <v-row id="partners" dense class="justify-center">
    <v-col v-for="i in partners" :key="i.id" loading cols="12" xs="6" sm="4" md="3" lg="2">
      <v-tooltip bottom>
        <template v-slot:activator="{ props }">
          <a :href="i.url" target="_blank" v-bind="props">
            <v-img height="50" contain :src="i.logo" :alt="i.name" :title="i.name"/>
          </a>
        </template>
        <span>{{ i.name }}</span>
      </v-tooltip>
    </v-col>
  </v-row>
</template>
<script setup lang="ts">
const {data: partners} = await useHttp('/api/v1/custom-content/partners/')
</script>

<style scoped>
#partners {
  border: 1px solid red;
}
</style>
