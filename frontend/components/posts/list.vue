<template>
  <v-card class="mx-auto">
    <v-card-title>News</v-card-title>
    <v-list v-if="posts.length > 0">
      <v-list-item v-for="post in posts" :key="post.id" :to="`/posts/${post.id}`">
        <v-list-item-title>
          {{ post.title }}
        </v-list-item-title>
        <v-list-item-subtitle>
          {{ post.intro }}
        </v-list-item-subtitle>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script setup>
const { data: posts } = await useFetch('/api/v1/custom-content/news/')
</script>
